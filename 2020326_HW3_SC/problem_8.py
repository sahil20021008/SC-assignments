import numpy as np


A=np.array([[2,3,2],[10,3,4],[3,6,1]])
eigenvalues, eigenvectors = np.linalg.eig(A.copy())
true_largest_eigenvalue=np.max(np.abs(eigenvalues))
x=np.array([0,0,1])
smallest_eigenvalue=0
rayleigh_shift=0
error_1=0
error_2=0
error_3=0
for i in range(50000):
    x_t=np.transpose(x)
    rayleigh_shift=np.matmul(x_t,np.matmul(A,x))/np.matmul(x_t,x)
    if np.linalg.det(A-rayleigh_shift*np.identity(3))==0:
        continue
    y=np.linalg.solve(A-np.identity(3)*rayleigh_shift,x)
    smallest_eigenvalue=1/np.linalg.norm(y,np.inf)
    x=y*smallest_eigenvalue
    smallest_eigenvalue=rayleigh_shift+smallest_eigenvalue
    if i==2:
        error_3=np.abs(np.abs(smallest_eigenvalue)-true_largest_eigenvalue)
    if i==0:
        error_1=np.abs(np.abs(smallest_eigenvalue)-true_largest_eigenvalue)
    if i==1:
        error_2=np.abs(np.abs(smallest_eigenvalue)-true_largest_eigenvalue)
final_rate=np.log(error_3/error_2)/np.log(error_2/error_1)
print("The results from implementing Rayleigh quotient iteration are:")
print("The eigenvalue is:",smallest_eigenvalue)
print("The corresponding eigenvector for the eigenvalue is:",x)
print("The rate of convergence is:",final_rate)

print("\nComparison:\n")
print("The results from using np.linalg.eig are:")
print("The eigenvalues from np.linalg.eig are:",eigenvalues)
print("The eigenvectors from np.linalg.eig are:",eigenvectors)
