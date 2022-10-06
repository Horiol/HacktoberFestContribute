def factorial(n):                       # helper function for calculating factorials
    return 1 if n == 0 else n * factorial(n-1)

def catalan_numbers(n):
    result = [0]*n                                                              # make the 'empty' result list length of n
    for i in range(n):
        result[i] = int(factorial(2*i) / (factorial(i + 1)*factorial(i)))       # calculate next catalan numbers, and append them to result list
    return (result)                                                             # yield the result list

# print catalan_numbers(10)             # test code

