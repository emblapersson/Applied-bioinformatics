# EXTRACT REGION BETWEEN PRIMERS
# A script to select the region between two given primers in a sequence, through pairwise alignment with a
# reference sequence in which the primers are known to be found
# Written partly with the help of ChatGPT

# Input:
# - input_sequences: A fastafile with the sequences of interest [.fasta]
# - reference_sequence: A fastafile with the reference sequence, where the primers are known to be found [.fasta]
# - forward_primer: The sequence of the forward primer
# - reverse_primer: The sequence of the reverse primer
# Output:
# - output_fasta: A fasta file with the extracted regions [.fasta]
# - output_missing: A txt file in which sequences where the primers couldn't be found will be stored [.txt]

# The program will go through each sequence separately and:
# 1) Align the sequence to the reference through pairwise alignment
# 2) Search for the primers in the reference sequence, in the alignment
# 3) If the primers are found, the positions in the alignment will be noted and the input sequence
# be cut at that position and the result written to the output_fasta file
# 4) If the primers aren't found, the sequence ID will be stored in the output_missing file
# ------------------------------------------------------------------------------------------------------

# TO BE SPECIFIED
# Input and output
input_sequences = '/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/01_Collect_sequences/02_Sequences/Correct_16S_sequences/All_correct_16S.fasta'
reference_sequence = '/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/01_Extract_regions/01_Input_data/Ecoli.fasta'
# V1V9
forward_primer = 'AGAGTTTGATCATGGCTCAG'
reverse_primer = 'GGTTACCTTGTTACGACTT'
# V3V4
# forward_primer = 'CCTACGGGAGGCAGCAG'
# reverse_primer = 'GACTACCAGGGTATCTAATCC'
output_fasta_file = '/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/01_Extract_regions/02_Output_data/All_correct_v1v9.fasta'
output_missing_file = '/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/01_Extract_regions/02_Output_data/All_correct_v1v9_missing.txt'

# ------------------------------------------------------------------------------------------------------
# Import packages
from Bio import SeqIO
from Bio.Align import PairwiseAligner

# Function definitions
def reverse_complement(sequence):
    '''
    Find the reverse complement of a given sequence.
    '''
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'N': 'N'}
    rev_compl = ''.join(complement[base] for base in reversed(sequence))
    return rev_compl

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

def extract_region_of_interest(seq, aligned_ref, aligned_query, ref_start, ref_end):
    """
    Extract the region of interest from the aligned query sequence based on reference coordinates.
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
    
    # Extract and return the region if both start and end were found
    # Otherwise, return None
    if query_start is not None and query_end is not None:
        return seq[query_start:query_end]
    return None

def process_sequences(input_seqs, reference_seq, forward_primer, reverse_primer, output_fasta_file, output_missing_file):
    """
    Extract sequences between primers based on alignment to a reference sequence.
    """
    # Start by converting the reverse primer, since we will only look at the forward strand
    reverse_primer_rev_compl = reverse_complement(reverse_primer)

    # Find positions of primers in the reference sequence
    ref_start = reference_seq.index(forward_primer) + len(forward_primer)
    ref_end = reference_seq.index(reverse_primer_rev_compl)

    # Write the extracted sequence to the output fasta file
    with open(output_fasta_file, "w") as out_fasta:
        with open(output_missing_file, 'w') as out_missing:
            for record in SeqIO.parse(input_seqs, "fasta"):
                seq = str(record.seq).upper()

                # Align sequence to reference
                aligned_ref, aligned_query = align_to_reference(seq, reference_seq)

                # Extract region of interest
                extracted_seq = extract_region_of_interest(seq, aligned_ref, aligned_query, ref_start, ref_end)

                # If the region was found, write it to the output file
                if extracted_seq:
                    out_fasta.write(f">{record.id}\n{extracted_seq}\n\n")
                
                # If it wasn't found, check if it can be found on the reverse complementary strand
                else:
                    reversed_seq = str(reverse_complement(record.seq).upper())
                    aligned_ref_rev, aligned_query_rev = align_to_reference(reversed_seq, reference_seq)
                    extracted_seq_rev = extract_region_of_interest(reversed_seq, aligned_ref_rev, aligned_query_rev, ref_start, ref_end)

                    if extracted_seq_rev:
                        out_fasta.write(f">{record.id}\n{extracted_seq_rev}\n\n")
                    else:
                        out_missing.write(f">{record.id}\n")

# ------------------------------------------------------------------------------------------------------
# Run the program
# Parse out the reference sequence
for record in SeqIO.parse(reference_sequence, "fasta"):
    ref_seq = record.seq

process_sequences(input_sequences, ref_seq, forward_primer, reverse_primer, output_fasta_file, output_missing_file)