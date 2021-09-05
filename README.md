# Computing Codon Usage Bias in Propionibacterium acidifaciens

The codon usage bias in the complete genome sequence of Propionibacterium acidifaciens and its four highly expressed genes — rsgA, clpB, rsfA, and dnaK — are calculated using Python. The aim of this work is to identify if the top-most frequent codon for each amino acid in the complete genome sequence is the same in these four highly expressed genes. Studies show that highly expressed genes contain a stronger codon usage bias due to the translational accuracy and efficiency of these frequent codons, explaining strong natural selection (Chen, et al., 2017). If the top-most frequent codons are (at least mostly) the same in the complete genome and the highly expressed genes, then the complete genome is typically inclined to bias for a codon despite the degree of expression of genes. Only a preliminary analysis is complete now. Additional analyses will be updated regularly.

Propionibacterium acidifaciens complete genome sequence: https://www.ncbi.nlm.nih.gov/nuccore/NZ_CP033719.1?report=gbwithparts&log$=seqview

rsgA gene sequence: https://www.ncbi.nlm.nih.gov/nuccore/NZ_LT593929.1?report=genbank&from=1396763&to=1397857

clpB gene sequence: https://www.ncbi.nlm.nih.gov/nuccore/NZ_LT593929.1?report=genbank&from=481531&to=484131

rsfA gene sequence: https://www.ncbi.nlm.nih.gov/nuccore/NZ_LT593929.1?report=genbank&from=1573966&to=1574349&strand=true

dnaK gene sequence: https://www.ncbi.nlm.nih.gov/protein/AYW77536.1


Chen, S., Li, K., Cao, W., Wang, J., Zhao, T., Huan, Q., ... & Qian, W. (2017). Codon-resolution analysis reveals a direct and context-dependent impact of individual synonymous mutations on mRNA level. Molecular biology and evolution, 34(11), 2944-2958.
