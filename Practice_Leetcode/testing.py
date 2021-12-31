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

<<<<<<< HEAD
for i in range(num_strings):
    print(s1)


arr = [1, 4, 3, 2]
arr = ["1", "2", "3"]

print(" ".join(arr))
'''
#input 
'''
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
'''
d = {}
c = input()
for i in range(c):
    l = input().split(" ",2)
    print(l)
    d.update({ l[0]:l[1]})

for i in range(c):
    t = input()
    if t in d:
        print(t+"="+d.get(t))
    else:
        print("Not Found")