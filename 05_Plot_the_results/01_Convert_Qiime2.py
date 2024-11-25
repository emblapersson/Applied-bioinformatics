# CONVERT QIIME2
# Script to take Qiime2 output (.tsv file) and read it so that it can be plotted later on

# Input:
# - qiime_taxonomy: A tsv file with the Qiime2 taxonomic classification
# Output:
# - output_taxonomy: The same taxonomy, but outputed in a format that can be plotted

# ------------------------------------------------------------------------------------------------------

# TO BE SPECIFIED
qiime_taxonomy = '/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad bioinformatik/Applied-bioinformatics/05_Plot_the_results/01_Data/metadata.tsv'
output_taxonomy = '/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad bioinformatik/Applied-bioinformatics/05_Plot_the_results/01_Data/metadata_converted.csv'

# ------------------------------------------------------------------------------------------------------

# Import packages
import pandas as pd
import regex as re

# Read the input data
qiime_reads = pd.read_csv(qiime_taxonomy, sep='\t', index_col='Feature ID', skiprows = [1])
dataset = qiime_reads.copy(deep=True)

# Divide the column "taxon" into the taxonomical levels
# Delete the original "taxon" column
taxonomic_levels = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']
dataset[taxonomic_levels] = qiime_reads['Taxon'].str.split(';', expand=True)
dataset.drop('Taxon', axis=1, inplace=True)

# Delete the taxonomical levels from the names (k__Bacteria --> Bacteria)
def rename(name):
    '''Deletes the taxonomical prefix in classifications
    k_Bacteria --> Bacteria
    '''
    if name:
        return re.sub('.{1}__', '', name)

# Loop through all classifications
for row in range(len(dataset)):
    for column in range(len(taxonomic_levels)):
        name = dataset.iloc[row, 1+column]
        dataset.iloc[row, 1+column] = rename(name)
    dataset.iloc[row, :] = dataset.iloc[row, :].str.strip()

dataset.to_csv(output_taxonomy)