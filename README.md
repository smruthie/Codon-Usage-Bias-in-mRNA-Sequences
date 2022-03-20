# Codon Frequencies in CLOCK Gene of *Homo sapiens*

Amino acids (with more than one codon encoding them) can choose one more than the other codons due to selection for efficient and accurate translation, i.e., amino acids show codon usage bias. This is more prevalant in highly expressed genes such as those encoding ribosomal proteins, chaperones, etc. The program in this repository calculates the percentage of codon frequencies for each amino acid in a coding sequence, and was tested on the [CLOCK gene sequence](https://www.ncbi.nlm.nih.gov/nuccore/NM_001267843.2?report=gbwithparts&log$=seqview) of *Homo sapiens* taken from NCBI's 'nucleotide' database. 

The CLOCK:Bmal1 complex in mammals exist in both the SCN and peripheral tissues. Given a 24-hour activity to maintain the circadian rhythm of an organism, it's logical to assume that the CLOCK genes are highly expressed. The top-most frequent codon of amino acids with two codons should be chosen over 70% of the time, and those of amino acids with more than two codons should be chosen over 60% of the time: this is the standard I chose for assessing codon usage bias. 

Not all amino acids show codon usage bias in the CLOCK gene, but a few of them do: Tyrosine, Asparagine, Glutamate, and Cysteine. Some amino acids showed bias by choosing a particular codon **much** lesser than the other codons: TCG in Serine (0.95%), CCG in Proline (4.3%), GCG in Alanine (2.7%), etc. However, more comparisons are required to see if all amino acids with 4-6 codons show bias by choosing some codons radically lesser than the others. If it does not, then it may support the hypothesis that CLOCK genes show some codon usage bias. 

Note: The program does not remove introns, so the imported file should strictly be a coding sequence. 
