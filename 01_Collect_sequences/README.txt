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