import numpy as np 
print("Input Vector: [1,1,1,-1]") 
ipvector = np.array([1,1,1,-1]).reshape(1,4) 
def activation(x): 
    if(x>0): return 1
    else: return 0
w=np.transpose(ipvector)*ipvector
for i in range(4): 
    for j in range(4): 
        if(i==j): 
            w[i][j]=0 
print("\n Weight Matrix: ")
print(w) 
ipvector = np.array([1,1,1,0]) 
print("Input vector in binary representation: ",ipvector) 
x=np.array([0,0,1,0]).reshape(1,4) 
y=x
for i in range(4): 
    yin = x[0][i] + np.dot(y,w[:,i]) 
    print("yin_",i+1,": ",yin) 
    y[0][i]=activation(yin) 
    print("Updated Y :",y) 
    if((y==ipvector).all()): 
        print("Hence y=input vector x, vector converge") 
        break