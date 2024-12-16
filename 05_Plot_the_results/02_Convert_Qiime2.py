# CONVERT QIIME2
# Script to take Qiime2 output (.tsv file) and read it so that it can be plotted later on

# Input:
# - qiime_taxonomy: A tsv file with the Qiime2 taxonomic classification
# Output:
# - output_taxonomy: The same taxonomy, but outputed in a format that can be plotted

# ------------------------------------------------------------------------------------------------------
# TO BE SPECIFIED
qiime_taxonomy = '/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/05_Plot_the_results/01_Data/Fasta_long_reads/Fasta_long_reads.tsv'
output_taxonomy = '/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/05_Plot_the_results/01_Data/Fasta_long_reads/Fasta_long_reads_fixed.csv'

# ------------------------------------------------------------------------------------------------------
# Import packages
import pandas as pd
import numpy as np
import regex as re

# ------------------------------------------------------------------------------------------------------
# Functions
# Delete the taxonomical levels from the names (k__Bacteria --> Bacteria)
def delete_prefix(name):
    '''Deletes the taxonomical prefix in classifications
    k_Bacteria --> Bacteria'''
    if type(name) == str:
        return re.sub('.{1}__', '', name)

# Take away things following _ (Akkermansia muciniphila_D_776786 --> Akkermansia muciniphila)
def extract_name(name):
    '''Deletes all characters following _
    Akkermansia muciniphila_D_776786 --> Akkermansia muciniphila'''
    if type(name) == str:
        return re.sub(r'_.*', '', name)

# ------------------------------------------------------------------------------------------------------

# Read the input data
# If there is a header in the tsv file, we need skiprows=1 (if one line)
qiime_reads = pd.read_csv(qiime_taxonomy, sep=' ', skiprows=1, header=None)
qiime_reads.columns = ['Feature ID', 'Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Genus1', 'Species', 'Confidence']
qiime_reads.set_index('Feature ID', inplace=True)
qiime_reads.drop('Genus1', axis=1, inplace=True)

# To find misplaced confidence values
# Loop through all columns except the first (Kingdom) and last two (Confidence and Species)
# For each row in each column, check if there is "__" in the name and the name isn't NaN
# If so, it is a confidence value. Move it to the last column
for column in qiime_reads.columns[1:-2]:
    for row in qiime_reads.index:
        value = qiime_reads.loc[row, column]
        # Check if value is a string before searching for '__'
        if isinstance(value, str) and '__' not in value:
            qiime_reads.loc[row, 'Confidence'] = value
            qiime_reads.loc[row, column] = np.NaN

# Take away all ";" and extra spaces
for column in qiime_reads.columns[:-1]:
    for row in qiime_reads.index:
        value = qiime_reads.loc[row, column]
        if isinstance(value, str):
            qiime_reads.loc[row, column] = value.replace(';', '').strip()

# Convert all confidence values from strings to floats
qiime_reads['Confidence'] = qiime_reads['Confidence'].apply(lambda x: float(x))

# Delete prefix and extract the names from each cell
for column in qiime_reads.columns[:-1]:
    for row in qiime_reads.index:
        value = delete_prefix(qiime_reads.loc[row, column])
        name = extract_name(value)
        qiime_reads.loc[row, column] = name

qiime_reads.to_csv(output_taxonomy)