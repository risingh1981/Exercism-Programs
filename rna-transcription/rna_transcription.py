def to_rna(dna_strand):
    conversion = {"G":"C", "C":"G", "T":"A", "A":"U"}
    rna_strand = []
    for char in dna_strand:
        rna_strand.append(conversion[char])

    return "".join(rna_strand)
