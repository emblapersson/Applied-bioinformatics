TO PERFORM TAXONOMIC ASSIGNMENT
Scripts:
- importing_sequences_script: Importing the simulated sequencing to QIIME2 and producing a summary of the data
- taxonomic_analysis_script: Denoising the data with DADA2, taxonomically assign the ASVs and producing a taxa-bar-plot

Sample information:
- The files for each sample are named with the simulated technique and numbered to indicate which sample

Folder structure:
- 01_Input_data:
        - A manifest file containing the sample id, absolute file path and direction of sequencing
        - Metadata containing the sample id, the simulated platforn, strategy, source, layout and composition of each sample
        
- 02_Output_data
        - A qza file containing the sequencing data
        - A qza file containing the ASV sequences
        - A qza file containing the feature table
        - A qza file containing the DADA2 running statistics
        - A qza file containing the classifier
        - A qza file containing the taxonomy

- 03_Results
        - A qzv file containing a summary of the data
        - A qzv file containing a summary of the DADA2 running statistics
        - A qzv file containing a summary of the feature table
        - A qzv file containing a summary of the ASV sequences
        - A qzv file containing the taxonomy
        - A qzv file containing the taxa bar plots
