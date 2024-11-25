# COLLECT SEQUENCES FROM NCBI
# A script to download the 16S rRNA gene for a given number of species from NCBI, as well as their taxonomic classification
# The program requires that biopython is installed

# Input:
# - input_species: A txt file with the organisms of interest at species or genus level
# Output:
# - output_fasta: All 16S rRNA genes in fasta format [.fasta]
# - output_taxonomy: The taxonomy of the organisms for which the 16S rRNA gene was collected [.csv]
# - not_found: All species specified in the input file but not found in the database [.txt]

# NCBI is searched to find 1) the fasta files of the 16S rRNA gene and 2) the taxonomy of the downloaded organisms
# Search with the filters:
# - Species = Bacteria
# - Source databases = RefSeq
# - Sequence length = [1300, 1800]
# ------------------------------------------------------------------------------------------------------

# TO BE SPECIFIED
# Input and output
input_species = '01_Input_data/Given_organisms_species_genus.txt'
output_folder = '02_Sequences/'
output_fasta_file = 'All_taxa_species_genus.fasta'
output_taxonomy_file = 'Taxonomy_species_genus.csv'
output_notfound_file = 'Not_found_species_genus.txt'

# N° sequences to download per species
seqs_per_species = 1

# Email for NCBI
email = 'clara.nordquist.1217@student.uu.se'

# ------------------------------------------------------------------------------------------------------
# Import packages
import pandas as pd
from Bio import Entrez
from Bio import SeqIO

# Read input data
organism_dataset = pd.read_csv(input_species, names=['Organisms'])
organisms = [a for a in organism_dataset.iloc[:, 0]]

# Define outputs
output_fasta = open(output_folder+output_fasta_file, 'w')
output_taxonomy = open(output_folder+output_taxonomy_file, 'w')
output_taxonomy.write(f'ID, Kingdom, Phylum, Class, Order, Family, Genus, Species\n')
output_notfound = open(output_folder+output_notfound_file, 'w')

# Loop through all species
# For each species, search NCBI and save the results
# Download the specified number of 16S rRNA sequences and save to output_fasta_file
# For each downloaded sequence, save the taxonomy of the organism to output_taxonomy_file
# If an organism isn't found, write it to the terminal and save it to output_notfound_file

for organism in organisms:
    Entrez.email = email

    # Define search term
    search_term = f'''(
    "{organism}"[Organism] AND 16S[All Fields] AND refseq[filter] AND 
    "1300"[SLEN] : "1800"[SLEN] AND bacteria[filter]
    )'''

    # Search NCBI
    stream = Entrez.esearch(db = 'nucleotide', term = search_term, usehistory = 'y', idtype = 'acc')
    search_results = Entrez.read(stream)
    stream.close()
    acc_list = search_results['IdList']
    webenv = search_results['WebEnv']
    query_key = search_results['QueryKey']
    
    # Download the 16S rRNA gene
    stream = Entrez.efetch(db = 'nucleotide', rettype = 'fasta', retmode = 'text', retmax = seqs_per_species, 
                           webenv = webenv, query_key = query_key, idtype = 'acc')
    data = stream.read()
    
    # If the organism is found
    if type(data) == str:
        output_fasta.write(data)

        # Download the taxonomy
        stream = Entrez.efetch(db = 'nucleotide', rettype = 'gb', retmode = 'text', retmax = seqs_per_species, 
                               webenv = webenv, query_key = query_key, idtype = 'acc')
        for record in SeqIO.parse(stream, 'genbank'):
            output_taxonomy.write(f'{record.id}, ')
            output_taxonomy.write(f'{str(record.annotations["taxonomy"]).replace("[", "").replace("]", "")}\n')
    
    # If the organism isn't found
    else:
        print(f'Warning: {organism} not found in database')
        output_notfound.write(f'{organism}\n')

output_fasta.close()
output_taxonomy.close()
output_notfound.close()