import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sp
k=6
while k<=15:
    A=np.array([[1,1]])
    A=np.concatenate((A,np.array([[10**(-k),0]])))
    A=np.concatenate((A,np.array([[0,10**(-k)]])))
    q,r=np.linalg.qr(A) 
    b=np.array([-10**(-k)])
    b=np.concatenate((b,np.array([1+10**(-k)])))
    b=np.concatenate((b,np.array([1-10**(-k)])))
    print("QR factorization (np.linalg.qr) and traingular solver (scipy.linalg.solve_triangular) for k=",k,":",sp.solve_triangular(r,np.matmul(q.T,b)))
    k+=1