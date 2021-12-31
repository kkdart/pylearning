'''
def rotLeft(a, d):
    d = d%len(a)
    a = a[d:]+a[:d]
    return(a)

a = [1, 2, 3, 4, 5]

print(rotLeft(a,6))


#String Slicing
num_strings = 2
s1 = "Hacker"
s2 = "Rank"

print(s1[::2],s1[1::2])
print(s1[::-1])  
'''