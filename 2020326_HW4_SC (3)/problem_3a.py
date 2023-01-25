import matplotlib.pyplot as plt
import numpy as np
x_coord=np.linspace(-1,1,500)
y_coord=[]
for i in range(500):
    y_coord.append(1/(1+25*pow(x_coord[i],2)))
x=np.linspace(-1,1,11)
y=[]
A=np.zeros((11,11))
b=np.zeros(11)
for i in range(11):
    y.append(1/(1+25*pow(x[i],2)))
    b[i]=y[i]
    for j in range(11):
        A[i,j]=pow(x[i],j)
sol1=np.linalg.solve(A,b)
interpolation_1=[]
for i in range(500):
    sum=0
    for j in range(11):
        sum+=sol1[j]*pow(x_coord[i],j)
    interpolation_1.append(sum)
x2=np.linspace(-1,1,21)
y2=[]
A=np.zeros((21,21))
b=np.zeros(21)
for i in range(21):
    y2.append(1/(1+25*pow(x2[i],2)))
    b[i]=y2[i]
    for j in range(21):
        A[i,j]=pow(x2[i],j)
sol2=np.linalg.solve(A,b)
interpolation_2=[]
for i in range(500):
    sum=0
    for j in range(21):
        sum+=sol2[j]*pow(x_coord[i],j)
    interpolation_2.append(sum)
plt.plot(x_coord,interpolation_1,label="Interpolation of Runge Function(n=11)")
plt.plot(x_coord,y_coord,label="Runge Function",linestyle="dashed")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Polynomial Interpolation of Runge Function(n=11)")
plt.legend()
plt.show()
plt.plot(x_coord,interpolation_2,label="Interpolation of Runge Function(n=21)")
plt.plot(x_coord,y_coord,label="Runge Function",linestyle="dashed")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Polynomial Interpolation of Runge Function(n=21)")
plt.legend()
plt.show()

