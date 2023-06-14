x1=[1,1,-1,-1]
x2=[1,-1,1,-1]
t=[-1,1,-1,-1]

w1=0
w2=0
b=0
yin=0
theta=float(input("Enter value of threshold: "))
alpha=int(input("Enter value of Learning rate: "))
epoch=int(input("Enter the number of epochs: "))

def activation(yin):
    if(yin>theta):
        return 1
    elif(yin<-theta):
        return -1
    else:
        return 0

for j in range(epoch):
    for i in range(4):
        yin=w1*x1[i]+w2*x2[i]+b
        y=activation(yin)
        if(y!=t[i]):
            w1=w1+alpha*t[i]*x1[i]
            w2=w2+alpha*t[i]*x2[i]
            b=b+alpha*t[i]

print("Final Weights are: ")
print("w1: ",w1)
print("w2: ",w2)
print("b: ",b)