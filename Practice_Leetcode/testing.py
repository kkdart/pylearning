'''
def rotLeft(a, d):
    d = d%len(a)
    a = a[d:]+a[:d]
    return(a)

a = [1, 2, 3, 4, 5]

print(rotLeft(a,6))
'''

#String Slicing
num_strings = 2
s1 = "Hacker"
s2 = "Rank"

for i in range(num_strings):
    print(s1)
