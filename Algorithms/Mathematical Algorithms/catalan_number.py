'''Python program to find catalan number'''
def fact(n):
    return 1 if n <= 1 else (n*fact(n-1))


'''Taking input from user'''
n=int(input('Enter a number'))
catalan_num = (1//(n+1))*(fact(2*n)//fact(n)*fact(n))

print(catalan_num)
