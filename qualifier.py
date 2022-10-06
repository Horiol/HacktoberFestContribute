"""
Created on Fri Oct 15 11:31:28 2018

@author: Ankit Karan
"""


a=int(input("a:"))
b=[]
k=0
for _ in range(a):
    x=int(input("x:"))
    y=int(input("y:"))
    b.extend(int(input()) for _ in range(x))
    for j in range(x):
        b.sort(reverse=True)
        if(b[j]>=b[y-1]):
            k=k+1
    print(k)
    k=0
