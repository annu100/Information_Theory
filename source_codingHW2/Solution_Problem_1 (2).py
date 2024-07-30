# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:09:54 2021

@author: Ritesh Kumar
"""
import numpy as np

p = np.array([ 0, 0.2667262398,0.3534364081+0.2667262398,0.379837352+0.3534364081+0.2667262398, 1 ])
p_in = p

#print(p[2]) 
str_1 = "cbcabbbbcb"
str_2 = "abcbcbcbcc"

a1 = len(str_1)
a2 = len(str_2)      
for i in range(a1):
    # print('value of string', str_1[i])
   if str_1[i] == 'a':
     p1 = p[1]
   elif str_1[i] == 'b':
     p1 = p[2]
   else:
    p1 = p[3]
   p_f = [p1*p[1], p1*p[2], p1*p[3]]



if  str_1[a1-1] == 'a':
     print(' Arithmetic code for the two sequences 1 is', p_f[0])
  
elif str_1[a1-1] == 'b':
     print(' Arithmetic code for the  sequences 1 is', p_f[1])
else :
     print(' Arithmetic code for the two sequences 1 is', p_f[2]) 
     
     
      
for i in range(a2):
   if str_2[i] == 'a':
     p1 = p[1]
   elif str_2[i] == 'b':
     p1 = p[2]
   else:
    p1 = p[3]
   p_f = [p1*p[1], p1*p[2], p1*p[3]]



if  str_2[a1-1] == 'a':
     print(' Arithmetic code for the  sequences 2 is', p_f[0])
  
elif str_1[a1-1] == 'b':
     print(' Arithmetic code for the  sequences 2 is', p_f[1])
else :
     print(' Arithmetic code for the two sequences 2 is', p_f[2])    
     
     
     
     
     
     
