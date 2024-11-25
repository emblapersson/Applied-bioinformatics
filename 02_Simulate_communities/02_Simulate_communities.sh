#!/bin/bash -l
# ------------------------------------------------------------------------------------------------------
# SIMULATE MOCK COMMUNITIES
# Creates mock communities with different organisms in different ratios

# Input:
# - SEQUENCE_FILE = Fasta file with sequences for all organisms of interest
# - RATIOS = A folder with csv files describing the ratio of different organisms
# for various community structures with 100 organisms
# Output:
# - MOCK_COMMUNITY = Fasta file with sequences corresponding to the given ratio for that community structure

# ------------------------------------------------------------------------------------------------------

# TO BE SPECIFIED
SEQUENCE_FILE=01_Input_data/All_taxa_species_genus.fasta
RATIOS=02_Ratios
OUTPUT_FOLDER=03_Mock_communities

# ------------------------------------------------------------------------------------------------------

# For all types of mock communities to construct
# Open the correct ratio file
# Remove any pre-existing output file
# Read the ratio file
# For each species in it with a count > 0, grep the first fasta sequence corresponding to it in the sequence file and
# add the fasta sequence to the output file as many times as specified in the ratio file
for ID in I-B II III-B IV-B V
do
    RATIO=$RATIOS/${ID}.csv
    rm ${ID}.fasta

    exec < $RATIO
    while IFS="," read -r rec_column1 rec_column2
    do
        SPECIES=$rec_column1
        COUNT=$rec_column2
        if (( $COUNT > 0 ))
        then
            NAME=$(grep -m 1 "$SPECIES" $SEQUENCE_FILE)
            for i in $(seq 1 $COUNT)
            do
                sed -n "/$NAME/,/^ *$/ {p; /^ *$/q; }" $SEQUENCE_FILE >> $OUTPUT_FOLDER/${ID}.fasta
            done
        fi
    done 
done