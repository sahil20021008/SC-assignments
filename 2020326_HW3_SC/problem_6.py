import numpy as np

A=np.array([[2,3,2],[10,3,4],[3,6,1]])
largest_eigenvalue=0
x=np.array([0,0,1])
for i in range(50000):
    y=np.matmul(A,x)
    largest_eigenvalue=np.linalg.norm(y,np.inf)
    x=y/largest_eigenvalue
print("The results from implementing normalized power iteration are:")
print("The magnitude of the largest eigenvalue is:",largest_eigenvalue)
print("The corresponding eigenvector for the largest eigenvalue is:",x)
print()
A=np.array([[2,3,2],[10,3,4],[3,6,1]])
smallest_eigenvalue=0
x=np.array([0,0,1])
for i in range(50000):
    y=np.linalg.solve(A,x)
    smallest_eigenvalue=1/np.linalg.norm(y,np.inf)
    x=y*smallest_eigenvalue
print("The results from implementing inverse iteration are:")
print("The magnitude of the smallest eigenvalue is:",smallest_eigenvalue)
print("The corresponding eigenvector for the smallest eigenvalue is:",x)

print("\nComparison:\n")
eigenvalues, eigenvectors = np.linalg.eig(A)
print("The results from using np.linalg.eig are:")
print("The eigenvalues from np.linalg.eig are:",eigenvalues)
print("The eigenvectors from np.linalg.eig are:",eigenvectors)
