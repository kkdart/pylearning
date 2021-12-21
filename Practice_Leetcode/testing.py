def rotLeft(a, d):
    d = d%len(a)
    a = a[d:]+a[:d]
    return(a)

a = [1, 2, 3, 4, 5]

print(rotLeft(a,6))