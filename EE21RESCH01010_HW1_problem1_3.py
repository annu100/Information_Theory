import numpy as np
import random
# import uniform distribution
from scipy.stats import uniform
#num_trials is sample size
# p is 4 length vector containing probabilities(pmf)
p=[1,0,0,0]#given distribution
num_trials=int(input("Enter number of samples to be printed a/c to pmf\n"))#global variable
cdfp=[0,0,0,0]
cdfp=np.cumsum(p)# Cummulative pdf of pmf given
#print(cdfp)
def randomsamples(num_trials,p):
 Samples=[x for x in range(num_trials)]# creating string array for storage of samples
 alpha=["1","b","c","d"]
 for i in range(num_trials):
      U=np.random.rand() #random number between 0 and 1
      if (U<=cdfp[0]):
         Samples[i]=alpha[0]
      elif (U>cdfp[0]) and (U<cdfp[1]):
         Samples[i]=alpha[1]
      elif (U>cdfp[1]) and (U<cdfp[2]):
         Samples[i]=alpha[2]
      elif (U>cdfp[2]):
         Samples[i]=alpha[3]
 Samples=str(Samples)
 return(Samples)
y=randomsamples(num_trials,p)
print(y)
