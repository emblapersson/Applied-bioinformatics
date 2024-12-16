#!/bin/bash -l 
#SBATCH -A uppmax2024-2-7
#SBATCH -M snowy
#SBATCH -p core 
#SBATCH -n 2
#SBATCH -t 05:00:00
#SBATCH -J Sequencing_simulation

cat $0

module load bioinfo-tools samtools/1.20 PBSIM3/3.0.4

conda init
conda activate /home/gahe8576/AppBio/Applied-bioinformatics/03_Simulate_sequencing/condaTestEnv

INPUT_DATA=/home/gahe8576/AppBio/Applied-bioinformatics/01_Extract_regions/02_Output_data

cd resultsHiFi
for i in $(ls $INPUT_DATA/Individual_v1v9/)
do
pbsim --strategy wgs --method qshmm --qshmm /home/gahe8576/AppBio/SeqSim/pbsim3/pbsim3/data/QSHMM-RSII.model --depth 2000 --genome $INPUT_DATA/Individual_v1v9/$i --prefix PacBio_${i}_v1v9 --pass-num 10
done

for i in $(ls $INPUT_DATA/Individual_v1v9/)
do
samtools view -b PacBio_${i}_v1v9_0001.sam > PacBio_${i}_v1v9.bam

ccs PacBio_${i}_v1v9.bam PacBio_HiFi_${i}_v1v9.fastq.gz
done
