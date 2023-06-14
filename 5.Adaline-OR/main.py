x1=[1,1,-1,-1]
x2=[1,-1,1,-1]
t=[1,1,1,-1]

w1=0.1
w2=0.1
b=0.1
yin=0.0
E=0.0

alpha=float(input("Enter value of Learning rate: "))
epoch=int(input("Enter the number of epochs: "))


for j in range(epoch):
    E=0.0
    for i in range(4):
        yin=w1*x1[i]+w2*x2[i]+b
        w1=w1+alpha*(t[i]-yin)*x1[i]
        w2=w2+alpha*(t[i]-yin)*x2[i]
        b=b+alpha*(t[i]-yin)
        E=E+(t[i]-yin)**2
    print("Mean Square Error of epoch",j+1,": ","%.3f" %E)

print("Final Weights are: ")
print("w1: ","%.4f" %w1)
print("w2: ","%.4f" %w2)
print("b: ","%.4f" %b)