import numpy as np
import random
from matplotlib import pyplot as plt
# import uniform distribution
from scipy.stats import uniform
#num_trials is sample size
# p is 3 length vector containing probabilities(pmf)
# X is random variable which has 3 outcomes
p=[0.04,0.08,0.88]#given distribution P(X=0)=0.04 ,P(X=1)=0.08 ,P(X=2)=0.88
num_trials=int(input("Enter number of samples to be printed a/c to pmf\n"))#global variable
cdfp=[0,0,0,0]
cdfp=np.cumsum(p)# Cummulative pdf of pmf given
#print(cdfp)
def randomsamples(num_trials,p):
 Samples=[x for x in range(num_trials)]# creating string array for storage of samples
 alpha=["0","1","2"]
 for i in range(num_trials):
      U=np.random.rand() #random number between 0 and 1
      if (U<=cdfp[0]):
         Samples[i]=alpha[0]
      elif (U>cdfp[0]) and (U<cdfp[1]):
         Samples[i]=alpha[1]
      elif (U>cdfp[1]):
         Samples[i]=alpha[2]
      
 Samples=str(Samples)
 return(Samples)
y=randomsamples(num_trials,p)
print("Generated samples according to the probability distribution is \n")
print(y)

