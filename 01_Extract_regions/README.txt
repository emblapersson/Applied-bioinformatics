TO EXTRACT REGIONS
Scripts:
- 01_Optimize primer sequences: Find the best subsequence of a given primer sequence, to be able to extract the most sequences from a given set using the 02_Extract_variable_regions.py script
- 02_Extract_variable_regions.py: Given a primer pair, extract the region between them using pairwise alignment against a reference sequence in which the primer sequences are known to be found

Folder structure:
- 01_Input_data: If you want to have any input data specific for this part (otherwise just refer to the correct folder directly in the script)
	- A fasta file with the used reference sequence (E. coli)

- 02_Output_data: The output folder
	- Fasta files with the extracted regions
	- Txt files with the sequences for which the region could not be found