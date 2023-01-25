import matplotlib.pyplot as plt
import numpy as np
import math

abs_error_list=[]
x_coord=[]
for i in range(1,16):
    h=pow(10,-i)
    forward=((math.exp(-math.sin(pow(1+h,3))/4)-math.exp(-math.sin(pow(1,3))/4))/h)
    exact=-pow(1,2)*math.exp(-math.sin(pow(1,3))/4)*math.cos(pow(1,3))*3/4
    abs_error=math.log10(abs((forward-exact)))
    x=math.log10(h)
    x_coord.append(x)
    abs_error_list.append(abs_error)
    print("For h=",h,":")
    print("log10(h)=",x)
    print("The forward difference approximation is",forward)
    print("The exact value is",exact)
    print("The absolute error is",abs_error)
plt.plot(x_coord,abs_error_list)
plt.xlabel("log10(h)")
plt.ylabel("log10(absolute error)")
plt.title("log10(absolute error) vs. log10(h)")
plt.show()
