#Program to find perfect numbers within a given range l,m (inclusive) in python

#This code is made for the issue #184(Print all the perfect numbers in a given range.)
l = int(input())
m = int(input())
perfect_numbers = []
if l > m:
    l, m = m, l
for j in range(l,m+1):
    
    divisor = [i for i in range(1,j) if j%i == 0]

    if sum(divisor) == j:
        perfect_numbers.append(j)
        print(f"Found a perfect Number: {str(j)}")

print(f"Perfect Numbers Found in the Range({l} & {m})are:", perfect_numbers)    
