


def KMPSearch(pattern, txt): 
    
    m = len(txt) 
    n = len(pattern)

    q = 0 # index for pattern[] 

    # Preprocess the pattern (calculate pm[] array) 
    pm = PartialMatchTableSimple(pattern)

    i = 0 # index for txt[] 
    while i < m: 
        if pattern[q] == txt[i]: 
            i += 1
            q += 1

        if q == n: 
            print ("Found pattern at index " + str(i-q) )
            q = pm[q-1] 

        # mismatch after q matches 
        elif i < m and pattern[q] != txt[i]: 
            # Do not match pm[0..pm[q-1]] characters
            if q != 0: 
                q = pm[q-1] 
            else: 
                i += 1
    return 


def PartialMatchTableSimple(pattern):
    n = len(pattern)
    pm = [0]*n
    k = 0
    
    for q in range (1, n):
        k=q
        while (k >0):
            prefix = pattern[0:k]
            suffix = pattern[q+1-k:q+1]
            if (prefix == suffix):
                break
            else:
                k -= 1
        pm[q] = k
    return pm

pattern = "TACTA"
txt = "TACTAGTACTACTA"
print (PartialMatchTableSimple(pattern))
KMPSearch(pattern, txt)