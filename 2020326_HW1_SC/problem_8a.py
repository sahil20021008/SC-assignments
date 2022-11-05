import numpy as np

def gaussian_elimination_without_partial_pivoting(A, b):
    n = np.shape(A)[0]
    for k in range(n-1):
        for i in range(k+1, n):
            a_temp = A[i, k]/A[k, k]
            A[i, k] = a_temp
            for j in range(k+1, n):
                A[i, j] = A[i, j] - a_temp*A[k, j]
            b[i] = b[i] - a_temp*b[k]

    x = np.zeros(n)
    x[n-1] = b[n-1]/A[n-1, n-1]

    for i in range(n-2, -1, -1):
        sum = b[i]
        for j in range(i+1, n):
            sum = sum - A[i, j]*x[j]
        x[i] = sum/A[i, i]
    return x

l=np.array([10,20,30,40])
for i in l:
    print("For n = ", i)
    A=np.random.random_sample((i,i))
    b=np.matmul(A,np.ones(i))
    x=np.ones(i)
    x_gaussian=gaussian_elimination_without_partial_pivoting(A.copy(),b.copy())
    cond=np.linalg.cond(A.copy())
    x_solve=np.linalg.solve(A.copy(),b.copy())
    print("For Random Matrix:","Condition Number = ", cond, "Error from unpivoted solve = ",np.linalg.norm(x-x_gaussian)/np.linalg.norm(x),"Residual from unpivoted solve = ",np.linalg.norm(np.matmul(A,x_gaussian)-b)/np.linalg.norm(A)*np.linalg.norm(x),"Error from solve = ",np.linalg.norm(x-x_solve)/np.linalg.norm(x),"Residual from solve = ",np.linalg.norm(np.matmul(A,x_solve)-b)/np.linalg.norm(A)*np.linalg.norm(x),sep="\n")
    A=np.zeros((i,i))
    for j in range(i):
        for k in range(i):
            A[j,k]=1/(j+k+1)
    b=np.matmul(A,np.ones(i))
    x=np.ones(i)
    x_gaussian=gaussian_elimination_without_partial_pivoting(A.copy(),b.copy())
    cond=np.linalg.cond(A.copy())
    x_solve=np.linalg.solve(A.copy(),b.copy())
    print("For Hilbert Matrix:","Condition Number = ", cond, "Error from unpivoted solve = ",np.linalg.norm(x-x_gaussian)/np.linalg.norm(x),"Residual from unpivoted solve = ",np.linalg.norm(np.matmul(A,x_gaussian)-b)/np.linalg.norm(A)*np.linalg.norm(x),"Error from solve = ",np.linalg.norm(x-x_solve)/np.linalg.norm(x),"Residual from solve = ",np.linalg.norm(np.matmul(A,x_solve)-b)/np.linalg.norm(A)*np.linalg.norm(x),sep="\n")
    A=np.ones((i,i))
    for j in range(i):
        for k in range(j):    
            A[j,k]=-1
    b=np.matmul(A,np.ones(i))
    x=np.ones(i)
    x_gaussian=gaussian_elimination_without_partial_pivoting(A.copy(),b.copy())
    cond=np.linalg.cond(A.copy())
    x_solve=np.linalg.solve(A.copy(),b.copy())
    print("For one,minus one Matrix:","Condition Number = ", cond, "Error from unpivoted solve = ",np.linalg.norm(x-x_gaussian)/np.linalg.norm(x),"Residual from unpivoted solve = ",np.linalg.norm(np.matmul(A,x_gaussian)-b)/np.linalg.norm(A)*np.linalg.norm(x),"Error from solve = ",np.linalg.norm(x-x_solve)/np.linalg.norm(x),"Residual from solve = ",np.linalg.norm(np.matmul(A,x_solve)-b)/np.linalg.norm(A)*np.linalg.norm(x),sep="\n")
