# SIMULATE COMMUNITY STRUCTURE
# Takes a CSV file describing the structure of different communities (rows) as the ratio of different species (columns)
# Outputs one csv file for each community, with count numbers for the species instead

# Input:
# - input_table: A csv file with the species of interest (columns), and their ratios in different communities (rows)
# Output:
# - One file for each community, describing the number of sequences for each species in a community of 100 (percentage)

# ------------------------------------------------------------------------------------------------------

# TO BE SPECIFIED
input_table = '/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad bioinformatik/Applied-bioinformatics/02_Simulate_communities/01_Input_data/Community_structures.csv'
output_folder = '/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad bioinformatik/Applied-bioinformatics/02_Simulate_communities/02_Ratios/'

# ------------------------------------------------------------------------------------------------------
# Load packages
import pandas as pd

# Read the input
frequency_table = pd.read_csv(input_table, sep=';')
frequency_table.set_index('sub CST', inplace=True)
frequency_table.replace(',', '.', regex=True, inplace=True)

# For each type of community, create a new csv file with only the species' names and their abundance in a community
# of 100 individuals (their percentage)
# Save the csv files in a given output folder
for community in frequency_table.index:
    freq = frequency_table.loc[community,:].apply(lambda x: float(x))
    freq = freq[:].apply(lambda x: int(100*x))
    name = (community + '.csv').replace(' ', '')
    freq.to_csv(output_folder+name, header=False)