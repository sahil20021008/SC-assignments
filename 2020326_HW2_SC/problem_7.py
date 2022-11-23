import matplotlib.pyplot as plt
import numpy as np

x_noisy=np.loadtxt("hw2_data_denoising.txt")
D=np.zeros((len(x_noisy)-1,len(x_noisy)))
for i in range(len(x_noisy)-1):
    D[i,i]=-1
    D[i,i+1]=1
plt.plot(x_noisy,label="Noisy Signal")
lambda_value=np.array([1,100,10000])
for i in range(len(lambda_value)):
    A=np.identity(len(x_noisy))+lambda_value[i]*np.matmul(D.T,D)
    x_denoised=np.linalg.lstsq(A,x_noisy.copy(),rcond=None)[0]
    plt.plot(x_denoised,label="Denoised Signal with lambda="+str(lambda_value[i]))
plt.xlabel("$n$")
plt.ylabel("$x_{noisy}$")
plt.legend()
plt.show()