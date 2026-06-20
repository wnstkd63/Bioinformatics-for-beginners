sequence = "ATGCGT"

complement = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}

reverse_complement = "".join(
    complement[base] for base in reversed(sequence)
)

print(reverse_complement)
