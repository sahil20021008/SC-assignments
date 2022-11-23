import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
k=6
while k<=15:
    A=np.array([[1,1]])
    A=np.concatenate((A,np.array([[10**(-k),0]])))
    A=np.concatenate((A,np.array([[0,10**(-k)]])))
    aTransposeA=np.matmul(A.T,A)
    b=np.array([-10**(-k),1+10**(-k),1-10**(-k)])
    if np.linalg.det(aTransposeA)==0:
        print("The matrix is singular")
    else:
        print("Normal equation (np.linalg.solve) for k=",k,":",np.linalg.solve(np.matmul(A.T,A),np.matmul(A.T,b)))
    k+=1
