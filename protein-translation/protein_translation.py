def proteins(strand):
    aminoacids = {"AUG":"Methionine", "UUU":"Phenylalanine", "UUC":"Phenylalanine", "UUA":"Leucine", "UUG":"Leucine", "UCU":"Serine", "UCC":"Serine", "UCA":"Serine", "UCG":"Serine", "UAU":"Tyrosine", "UAC":"Tyrosine", "UGU":"Cysteine", "UGC":"Cysteine", "UGG":"Tryptophan", "UAA":"STOP", "UAG":"STOP", "UGA":"STOP"}
    aaArr = []
    for i in range(0,len(strand)-1,3):
        if (aminoacids[strand[i:i+3]] != "STOP"):
            aaArr.append(aminoacids[strand[i:i+3]])
        else:
            break
    return aaArr
 
