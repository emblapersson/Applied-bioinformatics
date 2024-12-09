#!/bin/bash -l
# ------------------------------------------------------------------------------------------------------
# GET INDIVIDUAL FASTA FILES
# Script that extracts the individual fasta sequences from a file, and saves them as new files
# Input:
# - FILE_ALL = File with all fasta sequences
# Output:
# - Individual fasta files

# ------------------------------------------------------------------------------------------------------

# TO BE SPECIFIED
FILE_ALL=/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/01_Extract_regions/02_Output_data/All_taxa_species_genus_v3v4.fasta
OUTPUT_FOLDER=/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/01_Extract_regions/02_Output_data/Individual_v3v4

# ------------------------------------------------------------------------------------------------------

# Read the input file
# Extract each fasta sequence header
# Save the sequence and the header as a new fasta file, with the header ID as name

IFS=$'\n'
for NAME in $(grep '>' $FILE_ALL | sed 's/>//') 
do
    sed -n "/>$NAME/,/^ *$/ {p; /^ *$/q; }" $FILE_ALL > $OUTPUT_FOLDER/${NAME}.fasta
done