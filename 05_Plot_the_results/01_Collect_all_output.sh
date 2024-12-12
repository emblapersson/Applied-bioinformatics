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
INPUT_FOLDER=/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/04_Taxonomic_assignment/03_Results/Fasta_short_reads
TEMP_ZIP_FOLDER=/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/05_Plot_the_results/00_Temp_zip_folder
OUTPUT_FILE=/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/05_Plot_the_results/01_Data/Fasta_short_reads/Fasta_short_reads.tsv

# ------------------------------------------------------------------------------------------------------

# Add the file header to the top of the output file
echo "Feature ID    Taxon   Confidence" > $OUTPUT_FILE

for FILE in $(ls $INPUT_FOLDER)
do
    NAME=$(basename -s .qzv $FILE)
    cp $INPUT_FOLDER/${NAME}.qzv $TEMP_ZIP_FOLDER/${NAME}.zip

    UNZIPPED_NAME=$(unzip -Z -1 $TEMP_ZIP_FOLDER/${NAME}.zip | head -1 | sed 's/VERSION//')
    
    cd $TEMP_ZIP_FOLDER
    unzip -q $TEMP_ZIP_FOLDER/${NAME}.zip
    cd $UNZIPPED_NAME
    echo $(cat data/metadata.tsv | sed -n '1,2d;p') >> $OUTPUT_FILE
done

rm -r $TEMP_ZIP_FOLDER/*