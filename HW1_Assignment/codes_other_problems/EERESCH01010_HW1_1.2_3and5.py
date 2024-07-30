from scipy.stats import binom
n=17
r=6
p=0.3824772289
u=binom.cdf(r, n, p)
print(u)
n=1002
r=408
p=0.3824772289
v=binom.cdf(r, n, p)
print(v)
