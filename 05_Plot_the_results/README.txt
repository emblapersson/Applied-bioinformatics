TO PLOT THE RESULTS
Scripts:
- 01_Collect_all_output.sh: Combines the Qiime2 output tsv files into one big file
- 02_Convert_Qiime2.py: Takes the output tsv file from Qiime2, and converts it to a format that is compatible with the plot script
- 03_Plots.ipynb: A Jupyter notebook with scripts to plot different results

Folder structure:
- 01_Data: Classification files (output from 01_Collect_all_output.sh and 02_Convert_Qiime2.py) [.tsv]

- 02_Plots: Folder to save the plots in