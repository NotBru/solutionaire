from math import comb
import numpy as np

def Simplex(N, m):
    if N<=0:
        yield []
    if N==1:
        yield [m]
    else:
        for i in range(m+1):
            for j in Simplex(N-1, m-i):
                yield [i]+j

def FilteredSimplex(N, m, f):
    for elem in Simplex(N, m):
        if f(elem):
            yield elem

def prob(N, R):
    big_N = sum(N)
    big_R = sum(R)
    for n, r in zip(N, R):
        if r<0 or r>n:
            return 0
    return np.prod([ comb(n, r) for (n, r) in zip(N, R) ])/comb(big_N, big_R)

def at_least_one(N, m):
    return 1-sum(prob(N, mult)
                  for mult in FilteredSimplex(len(N), m, lambda x: 0 in x) )

m = 0
while at_least_one([10]*5, m)<.9:
    m += 1

print(
'''The number of balls for the probability to be at least 0.9 is {},
''''which gives a probability of {:.03f}'''.format(m, at_least_one([10]*5, m)))
