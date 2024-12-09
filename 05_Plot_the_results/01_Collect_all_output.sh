#!/bin/bash -l
# ------------------------------------------------------------------------------------------------------
# COLLECT ALL OUTPUT
# Collect multiple Qiime2 output files (.tsv) and put them into one tsv file

# Input:
# - SEQUENCE_MAP = Map with all tsv files
# Output:
# - COLLECTED_TSV = File with all individual .tsv files, and their title as Feature ID column

# ------------------------------------------------------------------------------------------------------

# TO BE SPECIFIED
SEQUENCE_MAP=/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/05_Plot_the_results/01_Data
OUTPUT_FILE=/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/05_Plot_the_results/01_Data/Collected.tsv

# ------------------------------------------------------------------------------------------------------

# Add the file header to the top of the output file
echo "Feature ID    Taxon   Confidence" > $OUTPUT_FILE

# Collect the sequences from each tsv file
for SEQ in $SEQUENCE_MAP/*.tsv
do
    sed -n '1,2d;p' $SEQ >> $OUTPUT_FILE
    echo -en '\n' >> $OUTPUT_FILE
done