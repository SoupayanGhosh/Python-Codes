import math

n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))

if math.gcd(n1, n2) == 1:
    print("They are Co-prime")
else:
   print("The yare not co-prime")
