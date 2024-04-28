from json import loads, dumps
from os.path import exists
from math import ceil

# Calculates if numbers are prime and appends them to primes list
def calc_new_primes(n, primes):
    current = primes[len(primes)-1]
    goal = current + n
    for i in range(n):
        num = i+current+1
        is_prime = True
        for x in primes:

            if num%x == 0:
                is_prime = False
                break
        if is_prime == True:
            primes.append(num)

    return primes
# Calculates prime factors of n
# does not repeat factors, e.g. 4 returns [2] not [2,2]
def calc_factors(n, primes):
    if primes[len(primes)-1]<n/2:
        delta = ceil(n/2-primes[len(primes)-1])
        calc_new_primes(delta,primes)
    factors=[x for x in primes if n%x==0]
    print(factors)
    return factors
    
if __name__ == '__main__':
    
    if not exists('primes.json'):
        with open('primes.json','w') as file:
            file.write('[2,3,5,7]')

    with open('primes.json','r') as file:
        primes = loads(file.read())
    
    if len(primes)<3: 
        primes = [2,3,5,7]
    
    calc_factors(5681,primes)

    with open('primes.json','w') as file:
        file.write(dumps(primes))

