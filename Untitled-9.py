codon_table =  {
'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'CGU':'R', 'CGC':'R',
'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 'UCU':'S', 'UCC':'S',
'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S', 'AUU':'I', 'AUC':'I',
'AUA':'I', 'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L',
'CUG':'L', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', 'GUU':'V',
'GUC':'V', 'GUA':'V', 'GUG':'V', 'ACU':'T', 'ACC':'T', 'ACA':'T',
'ACG':'T', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'AAU':'N',
'AAC':'N', 'GAU':'D', 'GAC':'D', 'UGU':'C', 'UGC':'C', 'CAA':'Q',
'CAG':'Q', 'GAA':'E', 'GAG':'E', 'CAU':'H', 'CAC':'H', 'AAA':'K',
'AAG':'K', 'UUU':'F', 'UUC':'F', 'UAU':'Y', 'UAC':'Y', 'AUG':'M',
'UGG':'W','UAG':'Stop', 'UGA':'Stop', 'UAA':'Stop'
}


def readfasta(lines):

    seq = []
    index = []
    seqplast = ""
    numlines = 0

    for i in lines:

        if '>' in i:

            index.append(i.replace("\n", "").replace(">", ""))

            seq.append(seqplast.replace("\n", ""))

            seqplast = ""

            numlines += 1

        else:

            seqplast = seqplast + i.replace("\n", "")

            numlines += 1

        if numlines == len(lines):

            seq.append(seqplast.replace("\n", ""))

    seq = seq[1:]

    return index, seq


def translation(seq):


    i = 0

    p = ""

    while i < len(seq)/3 - 1:

        n = seq[3 * i] +seq[3*i+1] + seq[3*i+2]

        r = codon_table[n]

        i += 1

        p = p + r

    return p



f = open('rosalind_splc.txt', 'r')

lines = f.readlines()

f.close()


(index, seq) = readfasta(lines)

totlaseq = seq[0]

introns = seq[1:]

for line in introns:

    n = len(line)

    i = 0

    while i < len(totlaseq) - n + 1:

        subseq = totlaseq[i:i + n]

        if subseq == line:

            newseq = totlaseq[:i] + totlaseq[i + n:]

            totlaseq = newseq
        i += 1



rnaseq = totlaseq.replace('T', 'U')

protein = translation(rnaseq)

print(protein)



f = open('output.txt', 'w')

f.write(protein)

f.close()