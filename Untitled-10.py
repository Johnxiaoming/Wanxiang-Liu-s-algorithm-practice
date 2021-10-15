def fac(n):
    if n <= 2:
        return n
    else:
        return n * fac(n-1)


def permutations(n):
    a = range(1, n+1)

    while True:
        yield a[:]

        k = l = None

        for i in range(0, len(a) - 1):
            if a[i] < a[i+1]:
                k = i

        if k == None:
            break

        for i in range(k + 1, len(a)):
            if a[k] < a[i]:
                l = i

        a[k], a[l] = a[l], a[k]
        a[k+1:] = reversed(a[k+1:])


if __name__ == "__main__":

    small_dataset = 3
    large_dataset = 6

    n = large_dataset

    print fac(n)
    for p in permutations(n):
        print ' '.join(map(str, p))