#!/bin/bash

# Input och output-filer
input_csv="feature-table.csv"
output_tsv="feature-table.tsv"

# Förbered en header för TSV-filen
echo -e "#OTU ID\tSample1" > $output_tsv

# Lägg till data med Feature IDs och counts
awk -F',' 'NR==2 {for (i=2; i<=NF; i++) print i-1"\t"$i}' $input_csv >> $output_tsv

echo "Konvertering klar: $output_tsv"
