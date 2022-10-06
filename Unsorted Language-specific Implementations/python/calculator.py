a=int(input())
b=int(input())
c=int(input())
print("choose any of the below operations:")
print("[A]dd\n[M]ultiply\nm[I]n\ne[X]it")
x=input("enter A, M, I or X:")
if x in ['A', 'a']:
    print(a+b+c)
elif x in ['M', 'm']:
    print(a*b*c)
elif x in ['I', 'i']:
    print(min(a,b,c))
elif x not in ['E', 'e']:
    print("error! invalid input")
    
