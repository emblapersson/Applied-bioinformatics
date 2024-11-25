TO COLLECT SEQUENCES
Scripts:
- Collect_sequences.py: Download the 16S rRNA gene and taxonomy for a given list of species and/or genus

Folder structure:
- 01_Input_data: 
	- A txt file with the species and/or genus of interest
	- (Metadata of sequences)

- 02_Sequences: The output folder
	- A fasta file with all 16S rRNA genes collected
	- A txt file with all species not found in the database (but specified in the input)
	- A csv file with the taxonomy of the downloaded organisms

- 03_Mock_communities: The final output from the bash script (02_Simulate_community.sh), that is the mock communities. One fasta file for each mock community, with the number of sequences for each species corresponding to what was stated in the ratio files.