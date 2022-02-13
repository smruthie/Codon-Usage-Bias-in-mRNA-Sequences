# Computing Codon Usage Bias in Propionibacterium acidifaciens

I calculated the highest codon frequency in *Propionibacterium acidifaciens'* complete genome and its four highly expressed genes: two ribosomes and two chaperones. I need to make some updates: the sequence before start site and after stop site need to be excluded for each gene. Once that's done, I can use this algorithm for any codon usage bias computation. 

Propionibacterium acidifaciens complete genome sequence: https://www.ncbi.nlm.nih.gov/nuccore/NZ_CP033719.1?report=gbwithparts&log$=seqview

rsgA gene sequence (sequence.txt): https://www.ncbi.nlm.nih.gov/nuccore/NZ_LT593929.1?report=genbank&from=1396763&to=1397857

clpB gene sequence (clpB.txt): https://www.ncbi.nlm.nih.gov/nuccore/NZ_LT593929.1?report=genbank&from=481531&to=484131

rsfA gene sequence (rsfA.txt): https://www.ncbi.nlm.nih.gov/nuccore/NZ_LT593929.1?report=genbank&from=1573966&to=1574349&strand=true

dnaK gene sequence (dnaK.txt): https://www.ncbi.nlm.nih.gov/protein/AYW77536.1
