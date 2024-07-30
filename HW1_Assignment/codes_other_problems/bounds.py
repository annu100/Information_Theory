import math
from math import sqrt

n=1002
p = 0.3824772289
m = n*p 
c = 409/m
m = n*p 
s2 = n*p*(1-p) 
s = sqrt(s2) 
def Markov(n, p, c):
  return (1-1.0/c)
def Chernoff(n, p, c):
  d = 1-c
  m = n*p
  return math.exp(-(d**2/2)*m)
def Chebyshev(n, p, c):
  m = n*p
  s = math.sqrt(n*p*(1-p))
  k = m*(1-c)/s
  return (1- 1/k**2)
print(Markov(n, p, c))
print(Chernoff(n, p, c))
print(Chebyshev(n, p, c))
