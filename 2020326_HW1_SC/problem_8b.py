import numpy as np

def gaussian_elimination_with_partial_pivoting(A, b):
    n = np.shape(A)[0]
    l=np.zeros(n, dtype=int)
    s=np.zeros(n)
    for i in range(n):
        l[i] = i
        s_max = 0
        for j in range(n):
            s_max = max(s_max, abs(A[i, j]))
        s[i] = s_max
    for k in range(n-1):
        r_max = 0
        j=0
        for i in range(k, n):
            r = abs(A[l[i], k]/s[l[i]])
            if r > r_max:
                r_max = r
                j = i
        l[k], l[j] = l[j], l[k]
        for i in range(k+1, n):
            a_mult = A[l[i], k]/A[l[k], k]
            A[l[i], k] = a_mult
            for j in range(k+1, n):
                A[l[i], j] = A[l[i], j] - a_mult*A[l[k], j]
    for k in range(n-1):
        for i in range(k+1, n):
            b[l[i]] = b[l[i]] - A[l[i], k]*b[l[k]]
    x = np.zeros(n)
    x[n-1] = b[l[n-1]]/A[l[n-1], n-1]
    for i in range(n-2, -1, -1):
        sum = b[l[i]]
        for j in range(i+1, n):
            sum = sum - A[l[i], j]*x[j]
        x[i] = sum/A[l[i], i]
    return x

l=np.array([10,20,30,40])
for i in l:
    print("For n = ", i)
    A=np.random.random_sample((i,i))
    b=np.matmul(A,np.ones(i))
    x=np.ones(i)
    x_gaussian=gaussian_elimination_with_partial_pivoting(A.copy(),b.copy())
    cond=np.linalg.cond(A.copy())
    x_solve=np.linalg.solve(A.copy(),b.copy())
    print("For Random Matrix:","Condition Number = ", cond, "Error from pivoted solve = ",np.linalg.norm(x-x_gaussian)/np.linalg.norm(x),"Residual from pivoted solve = ",np.linalg.norm(np.matmul(A,x_gaussian)-b)/np.linalg.norm(A)*np.linalg.norm(x),"Error from solve = ",np.linalg.norm(x-x_solve)/np.linalg.norm(x),"Residual from solve = ",np.linalg.norm(np.matmul(A,x_solve)-b)/np.linalg.norm(A)*np.linalg.norm(x),sep="\n")
    A=np.zeros((i,i))
    for j in range(i):
        for k in range(i):
            A[j,k]=1/(j+k+1)
    b=np.matmul(A,np.ones(i))
    x=np.ones(i)
    x_gaussian=gaussian_elimination_with_partial_pivoting(A.copy(),b.copy())
    cond=np.linalg.cond(A.copy())
    x_solve=np.linalg.solve(A.copy(),b.copy())
    print("For Hilbert Matrix:","Condition Number = ", cond, "Error from pivoted solve = ",np.linalg.norm(x-x_gaussian)/np.linalg.norm(x),"Residual from pivoted solve = ",np.linalg.norm(np.matmul(A,x_gaussian)-b)/np.linalg.norm(A)*np.linalg.norm(x),"Error from solve = ",np.linalg.norm(x-x_solve)/np.linalg.norm(x),"Residual from solve = ",np.linalg.norm(np.matmul(A,x_solve)-b)/np.linalg.norm(A)*np.linalg.norm(x),sep="\n")
    A=np.ones((i,i))
    for j in range(i):
        for k in range(j):    
            A[j,k]=-1
    b=np.matmul(A,np.ones(i))
    x=np.ones(i)
    x_gaussian=gaussian_elimination_with_partial_pivoting(A.copy(),b.copy())
    cond=np.linalg.cond(A.copy())
    x_solve=np.linalg.solve(A.copy(),b.copy())
    print("For one,minus one Matrix:","Condition Number = ", cond, "Error from pivoted solve = ",np.linalg.norm(x-x_gaussian)/np.linalg.norm(x),"Residual from pivoted solve = ",np.linalg.norm(np.matmul(A,x_gaussian)-b)/np.linalg.norm(A)*np.linalg.norm(x),"Error from solve = ",np.linalg.norm(x-x_solve)/np.linalg.norm(x),"Residual from solve = ",np.linalg.norm(np.matmul(A,x_solve)-b)/np.linalg.norm(A)*np.linalg.norm(x),sep="\n")
    