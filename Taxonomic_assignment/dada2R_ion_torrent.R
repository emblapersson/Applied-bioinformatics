# if (!require("BiocManager", quietly = TRUE))
#   install.packages("BiocManager")
# BiocManager::install(version = "3.18")
# 
# BiocManager::install("dada2", force = TRUE)
# install.packages("Rcpp")
# 
# if (!requireNamespace("devtools", quietly = TRUE)){install.packages("devtools")}
# devtools::install_github("jbisanz/qiime2R")
# 
# if (!requireNamespace("BiocManager", quietly = TRUE))
#   install.packages("BiocManager")
# 
# BiocManager::install("biomformat")

library(dada2)
library(qiime2R)
library(biomformat)

plotQualityProfile("SRR3225712.fastq.gz")

#Filtrering and trimning
outF <- filterAndTrim("SRR3225712.fastq.gz", "filtered.fastq", truncLen=240,
                      maxN=0, maxEE=2, truncQ=2, rm.phix=TRUE,
                      compress=TRUE, multithread=TRUE) # On Windows set multithread=FALSE
head(outF)

#Denoising
errF <- learnErrors("filtered.fastq",  multithread=TRUE, BAND_SIZE=32, HOMOPOLYMER_GAP_PENALTY=-1)
dadaF <- dada("filtered.fastq", err=errF, multithread=TRUE)
seqtab <- makeSequenceTable(dadaF)
seqtab.nochim <- removeBimeraDenovo(seqtab, method="consensus", multithread=TRUE, verbose=TRUE)

# Creatingr result-files for QIIME2
write_biom(seqtab.nochim, "feature-table.biom")
asv_seqs <- getSequences(seqtab.nochim)
write.table(asv_seqs, file="asv-sequences.fasta", quote=FALSE, col.names=FALSE)
