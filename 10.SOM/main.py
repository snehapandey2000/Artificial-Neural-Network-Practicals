import numpy as np 
ip = np.array([[0,0,1,1], [1,0,0,0], [0,1,1,0], [0,0,0,1]]) 
print("No of inputs:",4) 
print("No of Cluster:",2) 
print("Learning rate: ",0.5) 
alpha=0.5
def Euclidian_distance(x,w): 
    ans=0 
    for i in range(4): 
        ans=ans+(w[i]-x[i])**2 
    return ans 
def update(w,ip):
    for i in range(4): 
        w[i] = w[i] +0.5*(ip[i]-w[i]) 

w= np.array([[0.2,0.4,0.6,0.8], [0.9,0.9,0.5,0.3]]) 
print("Initial Weights") 
print(w) 
for i in range(4): 
    d1=Euclidian_distance(ip[i],w[0]) 
    d2=Euclidian_distance(ip[i],w[1]) 
    if(d1<d2): 
        update(w[0],ip[i]) 
    else: 
        update(w[1],ip[i]) 
    print("Updated Weights after input",i+1) 
    print(w)