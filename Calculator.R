name<-"Carlos Justo"
Student_number <- 10369317


factorial<- function(num){
  factorial = 1
  
  if(num < 0) {
    print("MATH ERROR, only natural numbers")
  } else if(num == 0) {
    print("The factorial of 0 is 1")
  } else {
    for(i in 1:num) {
      factorial = factorial * i
    }
    print(paste("The factorial of", num ,"is",factorial))
  }
}
add <- function(x, y) {
  #return(x + y)
  return(paste("the summation of",x,'+',y,'is',(x+y)))
}

subtract <- function(x, y) {
  return(paste('the subtraction of',x,'-',y,'is',(x - y)))
}

multiply <- function(x, y) {
  return(paste('the multiplication of',x,'*',y,'is',(x * y)))
}

divide <- function(x, y) {
 if (y==0){
  print ("Math error, is undifined")
}else{
    return(paste('the divition of',x,'between',y,'is',(x / y)))
}}

exponent <- function(x,y) {
  return(paste('the exponent of',x,'^',y,'is',(x^y)))
}

squareroot<- function(x) {
  if (x<0){
    print ("Math ERRor, only natural numbers unless you are electritician")
  }else
  return(paste('the squarerrot of',x,'is', (sqrt(x))))
}

square<- function(x) {
  return(paste('the square of',x,'is',(x^2)))
}

cube <- function(x) {
  return(paste('the cube of',x,'is',(x^3)))
}


tangent <- function(x) {
  #specify when is undefined
  return(paste('the tangent of',x,'is',(tan(pi*x))))
}

log <- function(x){
  if (x<=0){
    print ("Math ERROR only natural numbers but zero")
  }else
  return(paste('the logarithm of',x,'is',(log10(x))))
}



#Calling all the functions with different case
print (factorial(0))
print (factorial(-5))
print(factorial(6))
print (add(4,9))
print (subtract(4,6))
print (multiply(7,9))
print (divide(10,9))
print (divide(4,0))
print (exponent(8,7))
print (squareroot(4))
print (squareroot(-9))
print (square(4))
print (cube(7))
print (tangent(45))
print (log(4))
print (log(-8))
print (log(0))
