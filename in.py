
n = int(input(" number : "))

for p in range( 2, int(pow(n,0.5)),1):
    if ((n % p)==0):
        isPrime = False

if (isPrime):
    print("Prime no.")
else:
    print("Not a prime no.")