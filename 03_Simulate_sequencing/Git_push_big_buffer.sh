#!/bin/bash -l 
#SBATCH -A uppmax2024-2-7
#SBATCH -M snowy
#SBATCH -p core 
#SBATCH -n 2
#SBATCH -t 30:00
#SBATCH -J test
#SBATCH --mail-type=ALL
#SBATCH --mail-user gslottner@gmail.com

cat $0
cd resultsHiFi
for i in $(ls *.fastq.gz)
do
git add $i

git commit -m "Terrible test."

git push
done
