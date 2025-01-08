# CONVERT ILLUMINA QIIME2 OUTPUT
# A script to convert the taxa bar plot csv file from Qiime2 where each sequence is a row
# and each taxonomic classification a column (and number of matching sequences cell values)

# Input:
# - input_taxonomy: A csv file with the taxa bar plot from Qiime2 [.csv]
# Output:
# - output_taxonomy: A csv file each sequence as a row, and its classification at different levels
# as columns

# ------------------------------------------------------------------------------------------------------

# TO BE SPECIFIED
# Input and output
in_file = '/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/05_Plot_the_results/01_Data/02_Simulated_reads/Illumina/Confidence_levels/Illumina_gg_80.csv'
out_file = '/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/05_Plot_the_results/01_Data/02_Simulated_reads/Illumina/Confidence_levels/Illumina_gg_80_clean.csv'

# ------------------------------------------------------------------------------------------------------
# Import packages
import pandas as pd

# Read the data
# Drop the last four columns ('Platform', 'Strategy', 'Source', 'Layout')
data = pd.read_csv(in_file, index_col='index')
data.drop(data.columns[-4:], axis=1, inplace=True)

# Find where there is a value in the dataset (represents a classification)
# Replace the value in those cells with their column name (= the classification)
a = data.where(data != 0).isnull()
for col in range(len(data.columns)):
    a.iloc[:, col].replace(False, data.columns[col], inplace=True)
a.replace(True, 0, inplace=True)

# Add a new column 'Taxonomy'
# For each row, add the value which is 0 to the new column
a['Taxonomy'] = a.apply(lambda row: next((val for val in row if val != 0), ''), axis=1)

# Take away "Illumina_" from the sequence names
a.index = a.index.str.replace('Illumina_', '')

# Convert the taxonomy column to a new dataset, and output it as the output csv
b = a['Taxonomy']
b.to_csv(out_file)