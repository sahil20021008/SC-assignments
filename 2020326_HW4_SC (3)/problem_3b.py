import matplotlib.pyplot as plt
import numpy as np

x_coord=np.linspace(-1,1,500)
y_coord=[]
for i in range(500):
    y_coord.append(1/(1+25*pow(x_coord[i],2)))

x=np.linspace(-1,1,11)
y=[]
A=np.zeros((40,40))
b=np.zeros(40)
for i in range(11):
    y.append(1/(1+25*pow(x[i],2)))
    b[i]=y[i]
for i in range(10):
    for j in range(4):
        A[i,4*i+j]=pow(x[i],j)
for i in range(4):
    A[10,36+i]=pow(x[10],i)
for i in range(9):
    for j in range(4):
        A[11+i,4*i+j]=pow(x[i+1],j)
        A[11+i,4*i+j+4]=-pow(x[i+1],j)
for i in range(9):
    for j in range(1,4):
        A[20+i,4*i+j]=j*pow(x[i+1],j-1)
        A[20+i,4*i+j+4]=-j*pow(x[i+1],j-1)
for i in range(9):
    for j in range(2,4):
        A[29+i,4*i+j]=j*(j-1)*pow(x[i+1],j-2)
        A[29+i,4*i+j+4]=-j*(j-1)*pow(x[i+1],j-2)
for i in range(1,4):
    A[38,i]=i*pow(x[0],i-1)
    A[39,36+i]=i*pow(x[9],i-1)
sol1=np.linalg.solve(A,b)
interpolation_1=[]
for i in range(500):
    sum=0
    for j in range(10):
        if x[j]<=x_coord[i]<=x[j+1]:
            for k in range(4):
                sum+=sol1[4*j+k]*pow(x_coord[i],k)
            interpolation_1.append(sum)
            break
plt.plot(x_coord,interpolation_1,label="Interpolation of Runge Function(n=11)")
plt.plot(x_coord,y_coord,label="Runge Function",linestyle="dashed")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Cubic Spline Interpolation of Runge Function(n=11)")
plt.legend()
plt.show()

x2=np.linspace(-1,1,21)
y2=[]
A2=np.zeros((80,80))
b2=np.zeros(80)
for i in range(21):
    y2.append(1/(1+25*pow(x2[i],2)))
    b2[i]=y2[i]
for i in range(20):
    for j in range(4):
        A2[i,4*i+j]=pow(x2[i],j)
for i in range(4):
    A2[20,76+i]=pow(x2[20],i)
for i in range(19):
    for j in range(4):
        A2[21+i,4*i+j]=pow(x2[i+1],j)
        A2[21+i,4*i+j+4]=-pow(x2[i+1],j)
for i in range(19):
    for j in range(1,4):
        A2[40+i,4*i+j]=j*pow(x2[i+1],j-1)
        A2[40+i,4*i+j+4]=-j*pow(x2[i+1],j-1)
for i in range(19):
    for j in range(2,4):
        A2[59+i,4*i+j]=j*(j-1)*pow(x2[i+1],j-2)
        A2[59+i,4*i+j+4]=-j*(j-1)*pow(x2[i+1],j-2)
for i in range(1,4):
    A2[78,i]=i*pow(x2[0],i-1)
    A2[79,76+i]=i*pow(x2[19],i-1)
sol2=np.linalg.solve(A2,b2)
interpolation_2=[]
for i in range(500):
    sum=0
    for j in range(20):
        if x2[j]<=x_coord[i]<=x2[j+1]:
            for k in range(4):
                sum+=sol2[4*j+k]*pow(x_coord[i],k)
            interpolation_2.append(sum)
            break
plt.plot(x_coord,interpolation_2,label="Interpolation of Runge Function(n=21)")
plt.plot(x_coord,y_coord,label="Runge Function",linestyle="dashed")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Cubic Spline Interpolation of Runge Function(n=21)")
plt.legend()
plt.show()