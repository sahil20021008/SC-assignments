import numpy as np
for j in range(0,21):
    x=np.pi/4+2*np.pi*10**j
    print("The value of j is", j)
    print("(x,tan(x) = (%1.16f,%1.16f)" % (x, np.tan(x)))
    print("Condition number is %1.16f" % (abs(x/(np.sin(x)*np.cos(x)))))
    print("Error in the input is", x*abs(np.tan(x)-1)/abs(x/(np.sin(x)*np.cos(x))))
