#!/bin/bash -l 
#SBATCH -A uppmax2024-2-7
#SBATCH -M snowy
#SBATCH -p core 
#SBATCH -n 2
#SBATCH -t 00:30:00
#SBATCH -J Sequencing_simulation
#SBATCH --mail-type=ALL
#SBATCH --mail-user gslottner@gmail.com

cat $0

module load bioinfo-tools python/3.9.5 biopython/1.80-py3.9.5 pysam/0.17.0-python3.9.5 PBSIM3/3.0.4

cd resultsPB

pbsim --strategy wgs --method qshmm --qshmm /home/gahe8576/private/AppBio/SeqSim/pbsim3/pbsim3/data/QSHMM-RSII.model --depth 10000 --genome ../../01_Extract_regions/02_Output_data/All_taxa_species_genus_v1v9.fasta

cd ../resultsILL

/home/gahe8576/.local/bin/iss generate --genomes ../../01_Extract_regions/02_Output_data/All_taxa_species_genus_v3v4.fasta -n 200000 --sequence_type amplicon --model miseq --output Illumina_v3v4_miseq
