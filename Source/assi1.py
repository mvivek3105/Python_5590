
def trip(t, n):
    temp = False
    for a in range(0, n - 2):

        for b in range(a + 1, n - 1):

            for c in range(b + 1, n):

                if (t[a] + t[b] + t[c] == 0):
                    print( t[a], t[b], t[c])
                    temp = True

    if (temp == False):
        print(" No triplets found ")


t = [int(x) for x in input().split()]
n = len(t)
trip(t, n)
