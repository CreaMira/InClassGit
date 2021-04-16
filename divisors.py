def printDivisors(n) :
    i = 1
    while i <= n :
        if (n % i==0) :
            print (i), 
        i = i + 1
         

print ("The divisors of 99 are: ")
printDivisors(99)