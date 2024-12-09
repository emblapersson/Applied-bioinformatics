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

for SEQ in $SEQUENCE_MAP/*.tsv
do
    echo $SEQ
done