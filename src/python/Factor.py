# Factor.py - factorization of integers

def factor(n):
    factors = []
    p = 2
    while n > 1:
        while n % p == 0:
            factors.append(p)
            n = n / p
        p = p + 1
    return factors

def isFactor(n, f):
    if(n % f == 0):
        return True
    else:
        return False

# Test code for factor()
print ('Factorization of 10, 100, 1000, 10000')
print (factor(10))
print (factor(100))
print (factor(1000))
print (factor(10000))

# Test code for isFactor()
print ('10 a factor of 100: ' + str(isFactor(100, 10)))
print ('6 a factor of 100: ' + str(isFactor(100, 6)))