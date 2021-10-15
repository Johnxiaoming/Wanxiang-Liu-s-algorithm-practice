def find_indices(t):
    index = {}
    for i, char in enumerate(t):
        if char not in index:
            index[char] = [i]
        else:
            index[char].append(i)
    return index



def find(needle, haystack):
    """
    Find the smallest number in the 
    haystack that is greater than needle.
    """
    lo = 0
    hi = len(haystack) - 1

    while lo <= hi:
        if lo == hi:
            if haystack[lo] > needle:
                return lo
            else:
                return -1
        elif lo + 1 == hi:
            if haystack[lo] > needle:
                return lo

            elif haystack[hi] > needle:
                return hi

            else:
                return -1
        else:
            mid = (lo + hi) / 2
            if haystack[mid] > needle:
                hi = mid
            else:
                lo = mid
    return -1

def find_spliced_motif(s, t):
    index = find_indices(s)
    answer = []
    after = -1

    for i, char in enumerate(t):
        curr_arr = index[char]
        candidate = find(after, curr_arr)
        if candidate == -1:
            return None
        else:
            answer.append(curr_arr[candidate])
            after = curr_arr[candidate]
    return " ".join(map(str, map(lambda x : x + 1, answer)))

print find_spliced_motif("CCATGTTCTCGTCACTTTAGACGGAGTGTCGTATAGATATTTCTGGGAGCTATGTGCAATTCTATCAACATTCGAGTATTGATGCTTGGGAGGCCGACGAGGGAAGTGCCTAGGTGACGCGAAAAGGTTGTAAGGTTCACTATCAGAGCACGACCCGAGGTCGTGTGAGCGGACCCCTACATGTTATATCCTGGAGCGATACTCCTACAGCCAACAAGGCTCGTGAGATTAACAAGCATGGTGCTTCATGGACGTGCATGAGGCCCGGGTGGTTATCAGGCTTGCAGGTCCGCACAATGGAGCTCTTATCCGATTGAGGTGCTAAGACAAGTGGACTAGGGGGTGTCAACTACGCCATGAGGGTACACTCCCGCAGTTGAGGAAGTCTCCCCTACCGGATCGGCTGCTTATTGACCATTTTTAAGACAGTGCCAAAGTCGATTGTTATGGCACGAAGTCAGGACTGTGTTCAGGAGTTAAGCAGATCGACACAGGACATCCGCATCCCGAGAGATGCATGCTTCTGATTGGTGTTTCCTGATACTCGACAGATGCCGTGCAATCGGCCTTGTGCGATCCCAAGGCAATGAGCGATGAAGGTGTTCTGTCGGTTCCGCTTTTGATCCTGGTAGTTGTTCCTCAAACTGTGCCTTTCGACGCCTGATCAAGATTATGTCGTTGAAGCTTACCGCCCAATAAGTGGACGGCAATGCAAACCCTATTATAAGACACATGGATCATCTCTACCCCGTCATCAAAGACAATGCGAGTTGTCAGTGCTCATATTCAAAGAAACCTGCAGTAAAAACAAGGCCTATCGAGATATTTCCGCTTTCGTCAAGTTGCGGCTTTTTGATACTAAACCCTCAGAGCAATCCTTCAATAGGTGTAGGACTTGTGAGGGGCCACGTTCTAGCTTACATGCTAATCAATGAG", "TGCGGGTGAATGGGTCGGTCTACAGCTCGCAATTTGCACAGGCGCCGATCCATGGCTGTCAAACCACAAGATGTG")