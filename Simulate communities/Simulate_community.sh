#!/bin/bash -l
FASTA_FILE=All_taxa_species_genus.fasta
SPECIES_NAMES=Species.txt
SPECIES_ABUNDANCE=IB.csv

exec < IB.csv
while IFS="," read -r rec_column1 rec_column2
do
    SPECIES=$rec_column1
    COUNT=$(( $rec_column2 * 100))
    echo "Species is : $SPECIES"
    echo "Count is : $COUNT"
done 

# rm test.txt

# Make a file with all fasta files for the species of interest
# Look in the SPECIES_NAMES file (just a list of all species)
# Take the first sequence for that species from FASTA_FILE and put it in test.txt
# IFS=$'\n'
# for SPECIES in $(cat $SPECIES_NAMES)
# do
#     NAME=$(grep -m 1 "$SPECIES" $FASTA_FILE)
#     sed -n "/$NAME/,/^ *$/ {p; /^ *$/q; }" $FASTA_FILE >> test.txt
# done