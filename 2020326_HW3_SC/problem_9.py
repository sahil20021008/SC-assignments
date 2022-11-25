import numpy as np
import scipy.linalg as la


A=np.array([[2,3,2],[10,3,4],[3,6,1]])
B=A.copy()
shape=np.shape(B)
for i in range(50000):
    shift=B[shape[0]-1,shape[1]-1]
    q,r=la.qr(B-shift*np.identity(shape[0]))
    B=np.matmul(r,q)+shift*np.identity(shape[1])

print("Using the matrix A from Q6:")
eigenvalues_6=[]
for i in range(shape[0]):
    eigenvalues_6.append(B[i,i])
print("The eigenvalues from the QR algorithm are:",eigenvalues_6)
eigenvalues, eigenvectors = np.linalg.eig(A.copy())
print("The eigenvalues using np.linalg.eig are:",eigenvalues)

A=np.array([[6,2,1],[2,3,1],[1,1,1]])
B=A.copy()
shape=np.shape(B)
for i in range(50000):
    shift=B[shape[0]-1,shape[1]-1]
    q,r=la.qr(B-shift*np.identity(shape[0]))
    B=np.matmul(r,q)+shift*np.identity(shape[1])
print("\nUsing the matrix A from Q7:")
eigenvalues_7=[]
for i in range(shape[0]):
    eigenvalues_7.append(B[i,i])
print("The eigenvalues from the QR algorithm are:",eigenvalues_7)
eigenvalues, eigenvectors = np.linalg.eig(A.copy())
print("The eigenvalues using np.linalg.eig are:",eigenvalues)
