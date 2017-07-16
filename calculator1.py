#Carlos Justo
#Student number:10369317
import math

def formulafactorial(n):
	return reduce(lambda x,y:x*y, [1]+range(1,n+1)) # using reduce and lambda 
	
def factorial(n):
	return map(formulafactorial,n)

def squareroot(a):
	return map(lambda n: math.sqrt(n),a)
	

def add(a,b):
	return map(lambda first, second:first + second,a,b)  


def addlist(a):
	return reduce(lambda x,y: x+y, a)


def subtract(a,b):
	return map(lambda first, second: first-second,a,b)


def multiply (a,b):
	return map(lambda first,second: first*second,a,b)


def divide (a,b):
	return map(lambda first,second: first/second,a,b)


def exponent(a,b):
	return map(lambda first,second: first**second,a,b) 

def even(a):
	return filter(lambda x: x%2-1,a)
	

def filterneg(a):
	return filter(lambda x:x>0,a)
	
def squareroot(a):

	if [a]<0:
		return "Math Error" # no defined yet
	return map(lambda a:math.sqrt(a),filterneg(a))


def square(first):
	return map(lambda first:first**2,first)
	
def cube(first):
	return map(lambda first:first**3,first)


def tang(first):
	if first==90.0 or first==-90.0 or first==270.0 or first==-270: #I wanted to validate for others degrees with a standard formula as tang(x) = pi/2 + n*pi
		return "Undefined"
	return map(lambda first:math.tan(math.radians(first)),first)
	

def log(first):

	return map(lambda first:math.log10(first),first)

def sin(first):
	return map(lambda first:math.sin(math.radians(first)),first)

def cos(first):
	return map(lambda first:math.cos(math.radians(first)), first)
	
def listcomp(a,b):
	return [(a,b) for a in range(1,10) for b in range(a,10) if math.sin(a)**2 + math.cos(b)**2 == 1]
	#return [(a,b) if sin**2(a) + cos**2(b) == 1]

	
def reducing(a):
	return reduce(lambda a,b: a if (a>b) else b,a)







