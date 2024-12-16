#!/bin/bash -l
# ------------------------------------------------------------------------------------------------------
# COLLECT QIIME2 OUTPUT
# Collect multiple Qiime2 output files (.qzv), convert them to zip files, unzip them and save the metadata.tsv
# file (with the taxonomic classification)

# Input:
# - SEQUENCE_MAP = Map with all tsv files
# - TEMP_ZIP_FOLDER = Temporary folder for unzipping
# Output:
# - COLLECTED_TSV = File with all individual .tsv files, and their title as Feature ID column

# ------------------------------------------------------------------------------------------------------

# TO BE SPECIFIED
INPUT_FOLDER=/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/04_Taxonomic_assignment/03_Results/fasta_pacbio_silva
TEMP_ZIP_FOLDER=/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/05_Plot_the_results/00_Temp_zip_folder
OUTPUT_FILE=/Users/claranordquist/Documents/Universitetet/HT24/Tillämpad_bioinformatik/Applied-bioinformatics/05_Plot_the_results/01_Data/Silva/Fasta_long_reads/Fasta_long_reads.tsv

# ------------------------------------------------------------------------------------------------------

# Add the file header to the top of the output file
echo "Feature ID    Taxon   Confidence" > $OUTPUT_FILE

# Loop over the files in the input folder
# Extract the file name, convert to zip, unzip, collect metadata file, save its content in OUTPUT_FILE
for FILE in $(ls $INPUT_FOLDER)
do
    NAME=$(basename -s .qzv $FILE)
    cp $INPUT_FOLDER/${NAME}.qzv $TEMP_ZIP_FOLDER/${NAME}.zip

    UNZIPPED_NAME=$(unzip -Z -1 $TEMP_ZIP_FOLDER/${NAME}.zip | head -1 | sed 's/checksums.md5//')
    
    cd $TEMP_ZIP_FOLDER
    unzip -q ${NAME}.zip
    cd $UNZIPPED_NAME
    echo $(cat data/metadata.tsv | sed -n '1,2d;p') >> $OUTPUT_FILE
done

# Remove zipped and unzipped data
rm -r $TEMP_ZIP_FOLDER/*