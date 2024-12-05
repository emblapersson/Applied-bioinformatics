#!/bin/bash -l 
#SBATCH -A uppmax2024-2-7
#SBATCH -M snowy
#SBATCH -p core 
#SBATCH -n 2
#SBATCH -t 00:45:00
#SBATCH -J Binning
#SBATCH --mail-type=ALL
#SBATCH --mail-user gslottner@gmail.com

cat $0

module load python/3.9.5 pysam/0.17.0-python3.9.5 bioinfo-tools biopython/1.80-py3.9.5 PBSIM3/3.0.4
