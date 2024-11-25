import pandas as pd

input_table = '01_Input_data/Community_structures.csv'
output_folder = '02_Abundances/'

# Read the input
# A csv table with the species (columns) and their frequencies in different communities (rows)
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