import math
import numpy as np

for i in range(2,66,2):
    width=(3-1)/i
    summation=0
    for j in range(1,int(1+i/2)):
        lower=1+2*(j-1)*width
        upper=1+2*j*width
        x1=((upper-lower)*(1/np.sqrt(3))+upper+lower)/2
        x2=(upper+lower-(upper-lower)*(1/np.sqrt(3)))/2
        summation+=((100/x1)*math.sin(10/x1)+((100/x2)*math.sin(10/x2)))*(upper-lower)/2
    rel_error=abs((summation+18.79829683678703)/-18.79829683678703)
    print("For n=",i,":")
    print("The interpolated value is",summation)
    print("The relative error is",rel_error)