import numpy as np
def discrete_entropy(P_x):
  length=P_x.shape[0]
  entropy=0
  for i in range(length):
    entropy+=-P_x[i]*np.log2(P_x[i])
  return entropy

def joint_discrete_entropy(P_x):
  length=P_x.shape[0]
  entropy=0
  for i in range(P_x.shape[0]):
    for j in range(P_x.shape[1]):
      entropy+=-P_x[i,j]*np.log2(P_x[i,j])
  return entropy

def conditional_entropy(P_x_y,P_x):
  entropy=0
  for i in range(P_x_y.shape[0]):
    for j in range(P_x_y.shape[1]):
      entropy+=-P_x_y[i,j]*np.log2(P_x_y[i,j]/P_x[i])
  return entropy

def mutual_information(P_x_y,P_x,P_y):
  entropy=0
  for i in range(P_x_y.shape[0]):
    for j in range(P_x_y.shape[1]):
      entropy+=P_x_y[i,j]*np.log2(P_x_y[i,j]/(P_x[i]*P_y[j]))
  return entropy
#P_y_given_x=np.array([0.3495208281020331,0.7666731025798746,0.41603867647796217,0.025543712399367285,0.16566927089911193,0.5250540391086606,
#0.6249354594985996,0.0676576265210135,0.05890728441337722])
P_y_given_x=np.array([0.3495208281020331,0.7666731025798746,0.41603867647796217,0.025543712399367285,0.16566927089911193,0.5250540391086606,
0.6249354594985996,0.0676576265210135,0.05890728441337722])
print("P_y_given_x",P_y_given_x)
P_x=np.array([0.017801792419628343,0.40490679910102106,0.5772914084793506])
print("P_x",P_x)
print("H(x)=",discrete_entropy(P_x))
temp=P_y_given_x.reshape(3,3)
print(temp)
P_x_y=np.zeros([3,3])
for i in range(P_x.shape[0]):
  for j in range(P_x.shape[0]):
    P_x_y[j,i] = temp[i,j]*P_x[j]
print("P_x_y=",P_x_y)
P_y=np.sum(P_x_y,0)
print("P_y=",P_y)
Px=np.sum(P_x_y,1)
print("P_x=",Px)
print("H(y)=",discrete_entropy(P_y))
print(np.sum(P_x_y,1))
print("H(x,y)=",joint_discrete_entropy(P_x_y))
print("H(y|x)=",conditional_entropy(P_x_y,P_x))
print("H(x|y)=",conditional_entropy(P_x_y,P_y))
print("I(X;Y)=",mutual_information(P_x_y,P_x,P_y))
