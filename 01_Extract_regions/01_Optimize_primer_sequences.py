# OPTIMIZE THE PRIMER SEQUENCES
# A script to find the best possible subsequence of a given primer sequence for a dataset, and a given
# reference sequence.

# Input:
# - input_sequences: A fastafile with the sequences of interest [.fasta]
# - reference_sequence: A fastafile with the reference sequence, where the primers are known to be found [.fasta]
# - forward_primer: The sequence of the forward primer
# - reverse_primer: The sequence of the reverse primer, given as if it was on the same strand as the forward primer
# - forward_primer_lengths: List of lengths of subsequences of the forward primer you want to try
# - reverse_primer_lengths: List of lengths of subsequences of the reverse primer you want to try
# Output:
# - optimized_primers: A csv file with all possible subset of primers with the specified lengths, and for how
# many of the given input sequences that primer pair doesn't work [.csv]

# The program works by:
# 1) Finding all possible subsequence primers of the given lengths
# 2) Looping through all combinations, and trying to extract the sequence using a slightly modified version
# of the 02_Extract_variable_regions.py script (THIS ISN'T OPTIMIZED TIMEWISE TO IT MAY TAKE A WHILE!!!!)
# 3) Calculates the number of sequences in which the primers cannot be found, and saves it in a dictionary
# 4) Writes the dictionary to a csv file
# ------------------------------------------------------------------------------------------------------

# TO BE SPECIFIED
# Input and output
input_sequences = '/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/01_Collect_sequences/02_Sequences/Downloaded_4dec/All_taxa_species_genus.fasta'
reference_sequence = '/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/01_Extract_regions/01_Input_data/Ecoli.fasta'
forward_primer = 'AGAGTTTGATCATGGCTCAG'
reverse_primer = 'AAGTCGTAACAAGGTAACC'
forward_primer_lengths = [4, 5, 6]
reverse_primer_lengths = [4, 5, 6]
optimized_primers_file = '/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/01_Extract_regions/02_Output_data/Optimized_primers_v1v9.csv'

# ------------------------------------------------------------------------------------------------------
# Import packages
from Bio import SeqIO
from Bio.Align import PairwiseAligner
import regex as re
from itertools import product
from csv import writer

# Function definitions
def find_primers(sequence, primer, length):
    '''
    Find all possible subsequences of a given length from a primer, that only exist once in 
    the reference organism.
    '''
    out_list = []

    # Loop through the length of the primer, and look at all possible subsequences of a given length
    # Save all subsequences that are found just once in the reference sequence
    for i in range(len(primer)-length):
        primer_subseq = primer[i:i+length]
        matches = re.findall(primer_subseq, sequence)
        if len(matches) == 1:
            out_list.append(primer_subseq)
    
    return out_list

def align_to_reference(query_seq, reference_seq):
    """
    Align the query sequence to the reference sequence and return alignment details.
    """
    aligner = PairwiseAligner()
    aligner.mode = 'global'
    aligner.match_score = 1
    aligner.mismatch_score = -1
    aligner.open_gap_score = -2
    aligner.extend_gap_score = -1

    alignment = aligner.align(reference_seq, query_seq)[0]  # Get the best alignment
    aligned_ref = alignment.aligned[0]
    aligned_query = alignment.aligned[1]
    
    return aligned_ref, aligned_query

def extract_start_end(aligned_ref, aligned_query, ref_start, ref_end):
    """
    Find the region of interest from the aligned query sequence based on reference coordinates.
    Return the start and end positions of this region (None if it isn't found)
    """
    query_start = None
    query_end = None

    # Map reference positions to query sequence positions
    for ref_range, query_range in zip(aligned_ref, aligned_query):
        # Check if the primer region falls within this reference range
        if ref_start >= ref_range[0] and ref_start < ref_range[1]:
            query_start = query_range[0] + (ref_start - ref_range[0])
        if ref_end > ref_range[0] and ref_end <= ref_range[1]:
            query_end = query_range[0] + (ref_end - ref_range[0])
    
    return query_start, query_end

def find_missing_sequences(fasta_file, reference_seq, primer_fwd, primer_rev):
    """
    Find sequences in a dataset for which the given primers cannot be found. 
    Return a dictionary with the sequence IDs, as well as information on which primer(s) cannot be found.
    """
    # Find positions of primers in the reference sequence
    ref_start = reference_seq.index(primer_fwd) + len(primer_fwd)
    ref_end = reference_seq.index(primer_rev)

    # A dictionary to save the sequences, as well as information on how the primers match (or mismatch)
    missing_seqs = {}

    # Loop through all sequences
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq).upper()

        # Align sequence to reference and find start and end position of the primers
        aligned_ref, aligned_query = align_to_reference(seq, reference_seq)
        start, end = extract_start_end(aligned_ref, aligned_query, ref_start, ref_end)

        if start is None or end is None:
            missing_seqs[record.id] = start, end
    
    return missing_seqs

# ------------------------------------------------------------------------------------------------------
# Parse out the reference sequence
for record in SeqIO.parse(reference_sequence, "fasta"):
    ref_seq = str(record.seq)

# Create all possible possible primer subsequences
# Forward
forward_primer_subseqs = {}
for length in forward_primer_lengths:
    forward_primer_subseqs[length] = find_primers(ref_seq, forward_primer, length)
forward_primers_all = [primer for length in forward_primer_subseqs.values() for primer in length]

# Reverse
reverse_primer_subseqs = {}
for length in reverse_primer_lengths:
    reverse_primer_subseqs[length] = find_primers(ref_seq, reverse_primer, length)
reverse_primers_all = [primer for length in reverse_primer_subseqs.values() for primer in length]

# Loop through all possible primer combinations
# Save the primer combination, the number of sequences in which the region of interest cannot be found, 
# and details about the binding (if just one of the primers cannot be found ie)
primers_errors = {}
for forward, reverse in list(product(forward_primers_all, reverse_primers_all)):
    errors = find_missing_sequences(input_sequences, ref_seq, forward, reverse)
    primers_errors[(forward, reverse)] = errors 

# Write the results to files
with open(optimized_primers_file, "w") as out_file:
    writer = writer(out_file)
    writer.writerow(['Primer pair', 'N° missing sequences', 'Missing sequences'])
    for primer, errors in primers_errors.items():
        writer.writerow([f'{primer}, {len(errors)}, ({errors})'])