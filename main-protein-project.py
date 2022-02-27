import collections

f = open('CLOCK gene.txt', 'r') # or insert any coding sequence file of your choice
with f as file:
    sequence = file.read().replace('\n', '')  # Takes \n away from sequence string

codons = [sequence[i:i + 3] for i in range(0, len(sequence), 3)]  # converts sequence in file into triples/codons
codons_count = collections.Counter(codons)  # sorts codon frequency from the whole file in descending order

phenylalanine_keys = ['TTT', 'TTC']
leucine_keys = ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG']
methionine_keys = ['ATG']
valine_keys = ['GTT', 'GTC', 'GTA', 'GTG']
serine_keys = ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']
proline_keys = ['CCT', 'CCC', 'CCA', 'CCG']
threonine_keys = ['ACT', 'ACC', 'ACA', 'ACG']
alanine_keys = ['GCT', 'GCC', 'GCA', 'GCG']
tyrosine_keys = ['TAT', 'TAC']
histidine_keys = ['CAT', 'CAC']
glutamine_keys = ['CAA', 'CAG']
asparagine_keys = ['AAT', 'AAC']
lysine_keys = ['AAA', 'AAG']
aspartate_keys = ['GAT', 'GAC']
glutamate_keys = ['GAA', 'GAG']
cysteine_keys = ['TGT', 'TGC']
tryptophan_keys = ['TGG']
arginine_keys = ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']
glycine_keys = ['GGT', 'GGC', 'GGA', 'GGG']

total_phenylalanine = total_leucine = total_methionine = total_valine = total_serine = total_proline = total_threonine = total_alanine = total_tyrosine = total_histidine = total_glutamine = total_asparagine = total_lysine = total_aspartate = total_glutamate = total_cysteine = total_tryptophan = total_arginine = total_glycine = 0

# Total number of each amino acid in the file to use later for calculating percentages
for i in phenylalanine_keys:
    total_phenylalanine += codons_count[i]
for i in leucine_keys:
	total_leucine += codons_count[i]
for i in methionine_keys:
	total_methionine += codons_count[i]
for i in valine_keys:
	total_valine += codons_count[i]
for i in serine_keys:
	total_serine += codons_count[i]
for i in proline_keys:
	total_proline += codons_count[i]
for i in threonine_keys:
	total_threonine += codons_count[i]
for i in alanine_keys:
	total_alanine += codons_count[i]
for i in tyrosine_keys:
	total_tyrosine += codons_count[i]
for i in histidine_keys:
	total_histidine += codons_count[i]
for i in glutamine_keys:
	total_glutamine += codons_count[i]
for i in asparagine_keys:
	total_asparagine += codons_count[i]
for i in lysine_keys:
	total_lysine += codons_count[i]
for i in aspartate_keys:
	total_aspartate += codons_count[i]
for i in glutamate_keys:
	total_glutamate += codons_count[i]
for i in cysteine_keys:
	total_cysteine += codons_count[i]
for i in tryptophan_keys:
	total_tryptophan += codons_count[i]
for i in arginine_keys:
	total_arginine += codons_count[i]
for i in glycine_keys:
	total_glycine += codons_count[i]

# Putting codons for each amino acid in descending order of frequency
phenylalanine = collections.Counter({k: codons_count[k]/total_phenylalanine*100 for k in phenylalanine_keys})
leucine = collections.Counter({k: codons_count[k]/total_leucine*100 for k in leucine_keys})
methionine = collections.Counter({k: codons_count[k]/total_methionine*100 for k in methionine_keys})
valine = collections.Counter({k: codons_count[k]/total_valine*100 for k in valine_keys})
serine = collections.Counter({k: codons_count[k]/total_serine*100 for k in serine_keys})
proline = collections.Counter({k: codons_count[k]/total_proline*100 for k in proline_keys})
threonine = collections.Counter({k: codons_count[k]/total_threonine*100 for k in threonine_keys})
alanine = collections.Counter({k: codons_count[k]/total_alanine*100 for k in alanine_keys})
tryosine = collections.Counter({k: codons_count[k]/total_tyrosine*100 for k in tyrosine_keys})
histidine = collections.Counter({k: codons_count[k]/total_histidine*100 for k in histidine_keys})
glutamine = collections.Counter({k: codons_count[k]/total_glutamine*100 for k in glutamine_keys})
asparagine = collections.Counter({k: codons_count[k]/total_asparagine*100 for k in asparagine_keys})
lysine = collections.Counter({k: codons_count[k]/total_lysine*100 for k in lysine_keys})
aspartate = collections.Counter({k: codons_count[k]/total_aspartate*100 for k in aspartate_keys})
glutamate = collections.Counter({k: codons_count[k]/total_glutamate*100 for k in glutamate_keys})
cysteine = collections.Counter({k: codons_count[k]/total_cysteine*100 for k in cysteine_keys})
tryptophan = collections.Counter({k: codons_count[k]/total_tryptophan*100 for k in tryptophan_keys})
arginine = collections.Counter({k: codons_count[k]/total_arginine*100 for k in arginine_keys})
glycine = collections.Counter({k: codons_count[k]/total_glycine*100 for k in glycine_keys})

print("PERCENTAGES OF CODON USAGE FREQUENCY", "\n")
print("Phenylalanine: ", phenylalanine)
print("Leucine: ", leucine)
print("Methionine: ", methionine)
print("Valine: ", valine)
print("Serine: ", serine)
print("Proline: ", proline)
print("Threonine: ", threonine)
print("Alanine: ", alanine)
print("Tyrosine: ", tryosine)
print("Histidine: ", histidine)
print("Glutamine: ", glutamine)
print("Asparagine: ", asparagine)
print("Lysine: ", lysine)
print("Aspartate: ", aspartate)
print("Glutamate: ", glutamate)
print("Cysteine: ", cysteine)
print("Tryptophan: ", tryptophan)
print("Arginine: ", arginine)
print("Glycine: ", glycine)

f.close()
