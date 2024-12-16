#!/bin/bash -l 
#SBATCH -A uppmax2024-2-7
#SBATCH -M snowy
#SBATCH -p core 
#SBATCH -n 2
#SBATCH -t 01:00:00
#SBATCH -J Sequencing_simulation

cat $0

module load bioinfo-tools python/3.9.5 biopython/1.80-py3.9.5 pysam/0.17.0-python3.9.5

INPUT_DATA=/home/gahe8576/AppBio/Applied-bioinformatics/01_Extract_regions/02_Output_data

cd resultsILL

for i in $(ls $INPUT_DATA/Individual_v3v4/)
do
/home/gahe8576/.local/bin/iss generate --genomes $INPUT_DATA/Individual_v3v4/$i -n 20000 --sequence_type amplicon --model novaseq --output Illumina_${i}_v3v4_miseq
done
