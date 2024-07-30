# -*- coding: utf-8 -*-
"""Info theory.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1emOM9swMcWZxxFfN5b2kjdnQHFfesey2
"""

import numpy as np
import matplotlib.pyplot as plt

"""# **Inputs**"""

#my input
p_yby_x=np.array([0.278949502963185,
                  0.634217552330063,
                  0.0868329447067516,
                  0.671118752402879,
                  0.0479569589458991,
                  0.280924288651222,
                  0.0499317446339357,
                  0.317825488724038,
                  0.632242766642027])
px=np.array([1/3,1/3,1/3])

h_bar=0
for i in range(0,9):
  #print('i=',i)
  h_bar+=p_yby_x[i]*np.log2(p_yby_x[i])
  #print('hxy=',hxy)
  #print('----------')
h_bar=-h_bar
print('H(X,Y)=',h_bar)

#annu
#p_yby_x=np.array([0.318234896304418,
#                  0.677895117624694,
#                  0.0038699860708877,
#                  0.50645783727311,
#                  0.296881658639237,
#                  0.196660504087653,
#                  0.175307266422471,
#                  0.0252232237360687,
#                  0.79946950984146])
#px=np.array([0.0537294320517572,0.345071492239468,0.601199075708775])

"""# **H(X)**"""

hx=0
for i in range(0,3):
  #print('i=',i)
  hx+=px[i]*np.log2(px[i])
  #print('hx=',hx)
  #print('----------')
hx=-hx
print('H(X)=',hx)

"""# **H(Y)**"""

py=np.array([p_yby_x[0]*px[0]+p_yby_x[1]*px[1]+p_yby_x[2]*px[2],
             p_yby_x[3]*px[0]+p_yby_x[4]*px[1]+p_yby_x[5]*px[2],
             p_yby_x[6]*px[0]+p_yby_x[7]*px[1]+p_yby_x[8]*px[2]])
hy=0
for i in range(0,3):
  #print('i=',i)
  hy+=py[i]*np.log2(py[i])
  #print('hy=',hy)
  #print('----------')
hy=-hy
print('H(Y)=',hy)

"""# **H(X,Y)**"""

hxy=0
pxy=np.array([p_yby_x[0]*px[0],p_yby_x[1]*px[1],p_yby_x[2]*px[2],
             p_yby_x[3]*px[0],p_yby_x[4]*px[1],p_yby_x[5]*px[2],
             p_yby_x[6]*px[0],p_yby_x[7]*px[1],p_yby_x[8]*px[2]])
print(pxy)
for i in range(0,9):
  #print('i=',i)
  hxy+=pxy[i]*np.log2(pxy[i])
  #print('hxy=',hxy)
  #print('----------')
hxy=-hxy
print('H(X,Y)=',hxy)

"""# **H(Y|X)**"""

h_y_by_x=0
for i in range(0,9):
  #print('i=',i)
  h_y_by_x+=pxy[i]*np.log2(p_yby_x[i])
  #print('h_y_by_x=',h_y_by_x)
  #print('----------')
h_y_by_x=-h_y_by_x
print('H(Y|X)=',h_y_by_x)

"""# **H(X|Y)**"""

p_xby_y=np.array([pxy[0]/py[0],pxy[1]/py[1],pxy[2]/py[2],
                  pxy[3]/py[0],pxy[4]/py[1],pxy[5]/py[2],
                  pxy[6]/py[0],pxy[7]/py[1],pxy[8]/py[2],])
print(p_xby_y)
h_x_by_y=0
for i in range(0,9):
  #print('i=',i)
  h_x_by_y+=pxy[i]*np.log2(p_xby_y[i])
  #print('h_x_by_y=',h_x_by_y)
  #print('----------')
h_x_by_y=-h_x_by_y
print('H(X|Y)=',h_x_by_y)

Ixy=hx-h_x_by_y
print('I(X;Y)=',Ixy)

print('H(X,Y)=H(X|Y)+H(Y)...',(h_x_by_y+hy))
print('H(X,Y)=H(Y|X)+H(X)...',(h_y_by_x+hx))

"""# **Plot of H2(p)**"""

p=np.linspace(0,1,50)
emp=1e-7
H_2_p=(-p*np.log2(p+emp)-(1-p+emp)*np.log2(1-p+emp))
plt.plot(p,H_2_p,marker='.')
plt.title('Entropy vs Probability Distribution')
plt.xlabel('p-->')
plt.ylabel('H2(p)=plog(p)+(1-p)log(1-p)')
plt.grid()
plt.show()

# p_x2_by_x1
A=np.array([0.460668419723799,
                     0.479372321068345,
                     0.0599592592078563,
                     0.436024397805216,
                     0.103055235954605,
                     0.460920366240179,
                     0.103307182470985,
                     0.41757244297705,
                     0.479120374551965])

p_ybyx=np.reshape(p_yby_x,(3,3))
print(p_ybyx)
px_mar=np.zeros(3)
py_mar=np.zeros(3)
for i in range(3):
  px_mar[i]=sum(p_ybyx[i,:])
  py_mar[i]=sum(p_ybyx[:,i])
print(px_mar)
print(py_mar)

np.linalg.inv(p_ybyx)