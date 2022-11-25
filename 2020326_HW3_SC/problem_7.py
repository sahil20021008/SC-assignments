import numpy as np
A=np.array([[6,2,1],[2,3,1],[1,1,1]])
x=np.array([1,1,1])
smallest_eigenvalue=0
for i in range(50000):
    y=np.linalg.solve(A-np.identity(3)*2,x)
    smallest_eigenvalue=1/np.linalg.norm(y,np.inf)
    x=y*smallest_eigenvalue
smallest_eigenvalue=2+smallest_eigenvalue
print("The results from implementing shifted inverse iteration are:")
print("The eigenvalue is:",smallest_eigenvalue)
print("The corresponding eigenvector for the eigenvalue is:",x)

print("\nComparison:\n")
eigenvalues, eigenvectors = np.linalg.eigh(A.copy())
print("The results from using np.linalg.eigh are:")
print("The eigenvalues from np.linalg.eigh are:",eigenvalues)
print("The eigenvectors from np.linalg.eigh are:",eigenvectors)