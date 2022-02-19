import collections

f = open('sequence.txt', 'r')
with f as file:
    sequence = file.read().replace('\n', '')  # Takes \n away from sequence string
n = 3
codons = [sequence[i:i + n] for i in range(0, len(sequence), n)]  # converts sequence in file into triples/codons
codons_count = collections.Counter(codons)  # sorts codon frequency from the whole file in descending order

phenylalanine_keys = ['TTT', 'TTC']
leucine_keys = ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG']
methionine_keys = ['ATG']
valine_keys = ['GTT', 'GTC', 'GTA', 'GTG']
serine_keys = ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']
proline_keys = ['CCT', 'CCC', 'CCA', 'CCG']
threonine_keys = ['ACT', 'ACC', 'ACA', 'ACG']
alanine_keys = ['GCT', 'GCC', 'GCA', 'GCG']
tryosine_keys = ['TAT', 'TAC']
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

phenylalanine = {k: codons_count[k] for k in phenylalanine_keys}
leucine = {k: codons_count[k] for k in leucine_keys}
methionine = {k: codons_count[k] for k in methionine_keys}
valine = {k: codons_count[k] for k in valine_keys}
serine = {k: codons_count[k] for k in serine_keys}
proline = {k: codons_count[k] for k in proline_keys}
threonine = {k: codons_count[k] for k in threonine_keys}
alanine = {k: codons_count[k] for k in alanine_keys}
tryosine = {k: codons_count[k] for k in tryosine_keys}
histidine = {k: codons_count[k] for k in histidine_keys}
glutamine = {k: codons_count[k] for k in glutamine_keys}
asparagine = {k: codons_count[k] for k in asparagine_keys}
lysine = {k: codons_count[k] for k in lysine_keys}
aspartate = {k: codons_count[k] for k in aspartate_keys}
glutamate = {k: codons_count[k] for k in glutamate_keys}
cysteine = {k: codons_count[k] for k in cysteine_keys}
tryptophan = {k: codons_count[k] for k in tryptophan_keys}
arginine = {k: codons_count[k] for k in arginine_keys}
glycine = {k: codons_count[k] for k in glycine_keys}

print("CODON USAGE FOR PROPIONIBACTERIUM ACIDIFACIENS COMPLETE GENOME")
print("Phenylalanine: ", collections.Counter(phenylalanine))
print("Leucine: ", collections.Counter(leucine))
print("Methionine: ", methionine)
print("Valine: ", collections.Counter(valine))
print("Serine: ", collections.Counter(serine))
print("Proline: ", collections.Counter(proline))
print("Threonine: ", collections.Counter(threonine))
print("Alanine: ", collections.Counter(alanine))
print("Tyrosine: ", collections.Counter(tryosine))
print("Histidine: ", collections.Counter(histidine))
print("Glutamine: ", collections.Counter(glutamine))
print("Asparagine: ", collections.Counter(asparagine))
print("Lysine: ", collections.Counter(lysine))
print("Aspartate: ", collections.Counter(aspartate))
print("Glutamate: ", collections.Counter(glutamate))
print("Cysteine: ", collections.Counter(cysteine))
print("Tryptophan: ", collections.Counter(tryptophan))
print("Arginine: ", collections.Counter(arginine))
print("Glycine: ", collections.Counter(glycine), "\n")

f.close()
