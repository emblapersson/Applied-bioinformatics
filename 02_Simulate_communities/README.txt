TO SIMULATE MOCK COMMUNITIES
Scripts:
- 01_Simulate_communities.py: Takes a CSV file describing the structure of different communities (rows) as the ratio of different species (columns). Outputs one csv file for each community, with count numbers for the species instead
- 02_Simulate_communities.sh: Reads the CSV files and constructs one fasta file for each mock community, with each species having a different number of sequences (corresponding to the structure)

Folder structure:
- 01_Input_data: 
	- A fasta file with sequences for all species of interest
	- A CSV file describing the community structure with the species names as columns, and their ratio in different community structures as rows
	- (Valencia_metadata, describing where the community ratios come from)

- 02_Ratios: Folder containing the output from the python script (01_Simulate_communities.py). For each community structure, one csv file with the species as rows, and their count number in a community of 100 individuals

- 03_Mock_communities: The final output from the bash script (02_Simulate_community.sh), that is the mock communities. One fasta file for each mock community, with the number of sequences for each species corresponding to what was stated in the ratio files.