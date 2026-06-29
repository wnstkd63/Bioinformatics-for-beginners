sequence = "ATGGCCAAATAATGACCTAA"

start_codon = "ATG"
stop_codons = ["TAA", "TAG", "TGA"]

i = 0

while i < len(sequence) - 2:

    codon = sequence[i:i+3]

    if codon == start_codon:

        j = i + 3

        while j < len(sequence) - 2:

            stop = sequence[j:j+3]

            if stop in stop_codons:

                print("ORF:", sequence[i:j+3])
                break

            j += 3

    i += 1
