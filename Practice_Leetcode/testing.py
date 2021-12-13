
'''
from math import pi

def test(sentence):
    s1 = sentence.split()
    s1.reverse()
    final = ""
    for i in s1:
        final += i.swapcase()+" "
    return final


sentence = "Coding IS Awesome"

print(test(sentence))

class Rectangle:
    a = 0
    b = 0
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def area(self):
        return (self.a*self.b)

class Circle:
    r = 0
    def __init__(self,r) -> None:
        self.r = r
    def area(self):
        return pi*(self.r^2)


def fizzBuzz(n):
    for i in range(1,n+1):
        p = ""
        if i%3 and i%5 !=0:
            p += str(i)
        if i%3 == 0:
            p += "Fizz"
        if i%5 == 0:
            p += "Buzz"
        print(p)

fizzBuzz(15)


def average(*nums):
    c=len(nums)
    print(c)
    if c == 0:
        return None
    s = 0
    for i in nums:
        s += i
    print(s)
    return round(float(s)/c,2)


def numCells(grid):
    res=0
    for i in range(len(grid)):
        for k in range(len(grid[0])):
            val=grid[i][k]
            flag = 1
            for ii in range(max(0,i-1),min(len(grid),i+2)):
                for kk in range(max(0,k-1),min(len(grid[0]),k+2)):
                    if (ii,kk)!=(i,k) and val<-grid[ii][kk]:
                        flag = 0
                        break
                if flag ==0:
                    break
            else:
                res+=1
        return res

'''

def staircase(n):
    for i in range(n):
        txt = ""
        spaces = n-i-1
        for j in range(spaces):
            txt+=" "
        for k in range(i+1):
            txt+="#"
        print(txt)

staircase(3)