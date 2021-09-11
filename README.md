# Computing Codon Usage Bias in Propionibacterium acidifaciens

The codon usage bias in the complete genome sequence of Propionibacterium acidifaciens and its four highly expressed genes — rsgA, clpB, rsfA, and dnaK — are calculated using Python. The aim of this work was to identify if the top-most frequent codon for each amino acid in the complete genome sequence is the same in these four highly expressed genes. Studies show that highly expressed genes contain a stronger codon usage bias due to the translational accuracy and efficiency of these frequent codons, explaining strong natural selection (Chen, et al., 2017). If the top-most frequent codons are (at least mostly) the same in the complete genome and the highly expressed genes, then the complete genome is typically inclined to bias for a codon despite the degree of expression of genes. 

# Top-Most Frequent Codon for Each Amino Acid in the Completed Genome (Green) and the Highly-Expressed Genes (Blue)

![55817897-4C2A-4EBA-B1A9-65B0C169E9CF](https://user-images.githubusercontent.com/70722786/132909851-7a02898f-c7fc-402d-8066-5c446a6193c9.jpeg)

Propionibacterium acidifaciens complete genome sequence: https://www.ncbi.nlm.nih.gov/nuccore/NZ_CP033719.1?report=gbwithparts&log$=seqview

rsgA gene sequence (sequence.txt): https://www.ncbi.nlm.nih.gov/nuccore/NZ_LT593929.1?report=genbank&from=1396763&to=1397857

clpB gene sequence (clpB.txt): https://www.ncbi.nlm.nih.gov/nuccore/NZ_LT593929.1?report=genbank&from=481531&to=484131

rsfA gene sequence (rsfA.txt): https://www.ncbi.nlm.nih.gov/nuccore/NZ_LT593929.1?report=genbank&from=1573966&to=1574349&strand=true

dnaK gene sequence (dnaK.txt): https://www.ncbi.nlm.nih.gov/protein/AYW77536.1


Chen, S., Li, K., Cao, W., Wang, J., Zhao, T., Huan, Q., ... & Qian, W. (2017). Codon-resolution analysis reveals a direct and context-dependent impact of individual synonymous mutations on mRNA level. Molecular biology and evolution, 34(11), 2944-2958.
