x = 5
y=9
x+y
print(x+y)
name = "Bhuvi"
print(name)
print(name[-1])
print(name[:4] +"anesh")
# strings are immutable 
print(x/y)
print(x//y)

def fib(n):
    first=2
    second =3
    print(first)
    print(second)
    for i in range(1,n):
        
        c = first + second
        first = second
        second=c
        print(c)
fib(5)

def fact(n):
    fact =1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)
fact(6)

def fact(n):
    if(n==0):
        return 1
    return n * fact(n-1)
print(fact(6))


#functions without names is ananymous functions eg
f = lambda x: x**2
print(f(5))

#filter()
#inbuilt method used to filter the values based on condition which should be defined
#eg
numbers = [1, 2, 3, 4, 5, 6]
def even(n):
    return n % 2 == 0
evens = list(filter(even, numbers))
print(evens)

#map() is used make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.
#eg
doubles = list(map(lambda n:n+2, numbers))
print(doubles)

#similarly reduce() also performs a method with function that is used to perform operations 

#decorators
#decorators used to add extra methods for existing function without creatong new one
#eg

#modules
#import calc as c
#c.add(3,5)

from  functools import reduce
f = reduce(lambda a,b : a*b,[1,2,3,4,5])
print(f)
