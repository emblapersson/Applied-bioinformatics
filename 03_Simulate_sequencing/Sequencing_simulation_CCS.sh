#!/bin/bash -l 
#SBATCH -A uppmax2024-2-7
#SBATCH -M snowy
#SBATCH -p core 
#SBATCH -n 2
#SBATCH -t 05:00:00
#SBATCH -J Sequencing_simulation
#SBATCH --mail-type=ALL
#SBATCH --mail-user gslottner@gmail.com

cat $0

module load bioinfo-tools

conda init
conda activate /home/gahe8576/AppBio/Applied-bioinformatics/03_Simulate_sequencing/condaTestEnv

INPUT_DATA=/home/gahe8576/AppBio/Applied-bioinformatics/01_Extract_regions/02_Output_data

cd resultsHiFi

for i in $(ls $INPUT_DATA/Individual_v1v9/)
do
ccs PacBio_${i}_v1v9.bam PacBio_HiFi_${i}_v1v9.fastq.gz
done
