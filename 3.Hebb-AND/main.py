x1=[1,1,-1,-1]
x2=[1,-1,1,-1]
y=[1,-1,-1,-1]
w1=0
w2=0
b=0
epoch=int(input("Enter number of  epochs: "))

for i in range(epoch):
    for j in range(4):
        w1=w1+x1[j]*y[j]
        w2=w2+x2[j]*y[j]
        b=b+y[j]

print("Final weights are: ")
print("w1: ",w1)
print("w2: ",w2)
print("b: ",b)