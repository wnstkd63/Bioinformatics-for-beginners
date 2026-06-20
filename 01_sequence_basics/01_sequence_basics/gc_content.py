sequence = "ATGCGGATCCATGCGATCGATCG"

gc_count = sequence.count("G") + sequence.count("C")

gc_content = gc_count / len(sequence) * 100

print(f"GC content: {gc_content:.2f}%")
