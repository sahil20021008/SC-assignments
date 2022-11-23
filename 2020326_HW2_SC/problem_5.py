import matplotlib.pyplot as plt
import numpy as np

t,y=np.loadtxt('hw2_data_ty.txt',unpack=True)
s=np.log(y/(1-y))
A=np.array([np.ones(len(t)),t]).T
x_coordinate=np.linalg.solve(np.matmul(A.T,A),np.matmul(A.T,s))
x_coordinate_2=np.linalg.lstsq(A,s,rcond=None)[0]
error_1=np.linalg.norm(np.matmul(A,x_coordinate)-s)
error_2=np.linalg.norm(np.matmul(A,x_coordinate_2)-s)
print("The error while using the normal equation (np.linalg.solbe) is",abs(error_1))
print("The error while directly solving (np.linalg.lstsq) is",abs(error_2))
plt.plot(t,np.exp(x_coordinate[0]+x_coordinate[1]*t)/(1+np.exp(x_coordinate[0]+x_coordinate[1]*t)),label='Normal Equation')
plt.plot(t,np.exp(x_coordinate_2[0]+x_coordinate_2[1]*t)/(1+np.exp(x_coordinate_2[0]+x_coordinate_2[1]*t)),label='Direct Solve')
plt.plot(t,y,'o',label='Original Data')
plt.xlabel("$t_i$")
plt.ylabel("$f(t_i)$")
plt.legend()
plt.show()