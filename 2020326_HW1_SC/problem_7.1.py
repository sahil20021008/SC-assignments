import math 
print("Using equation 6.1")
for n in range(1,5001):
    partial_sum=0
    for k in range(1,n+1):
        partial_sum+=1/k
    if n%100==0: print("current n is", n, "and the value of term is", partial_sum-math.log(n))
