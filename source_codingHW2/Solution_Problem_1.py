# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:09:54 2021

@author: Ritesh Kumar
"""
import numpy as np

p = np.array([ 0.4,0.4,	0.2])
p_in = p

#print(p[2]) 
str_1 = "acaa"
str_2 = "caabccaacc"

a1 = len(str_1)
a2 = len(str_2)      
for i in range(a1):
    # print('value of string', str_1[i])
   if str_1[i] == 'a':
     p1 = p[1]
   else:
     p1 = p[2]
   p_f = [p1*p[1], p1*p[2]]



if  str_1[a1-1] == 'a':
     print(' Arithmetic code for the two sequences 1 is', p_f[0])
  
elif str_1[a1-1] == 'b':
     print(' Arithmetic code for the  sequences 1 is', p_f[1])
else :
     print(' Arithmetic code for the two sequences 1 is', p_f[2]) 
     
     
      

     
     
     
     
