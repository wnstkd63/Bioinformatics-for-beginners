codon_table = {
    "ATG": "M",
    "GCC": "A",
    "AAA": "K"
}

sequence = "ATGGCCAAA"

protein = ""

for i in range(0, len(sequence), 3):
    codon = sequence[i:i+3]
    protein += codon_table.get(codon, "X")

print(protein)
