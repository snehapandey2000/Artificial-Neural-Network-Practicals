x1 = [0,0,1,1]
x2 = [0,1,0,1]
z1 = [0,0,0,0]
z2 = [0,0,0,0]
y =  [0,1,1,0]
z =  [0,0,0,0]
yin1=0
yin2=0
yin=0

print("Enter Weights and threshold for hidden layer")
w11=int(input("Enter weight w11: "))
w21=int(input("Enter weight w21: "))
theta1=int(input("Enter threshold theta1: "))
w12=int(input("Enter weight w12: "))
w22=int(input("Enter weight w22 "))
theta2=int(input("Enter threshold theta2: "))


print("Enter weights for output layer")
w1=int(input("Enter weight w1: "))
w2=int(input("Enter weight w2: "))
theta=int(input("Enter threshold theta: "))

for x in range(4):

    yin1=w11*x1[x]+w21*x2[x]
    #print("yin1 :",yin1)
    if(yin1>=theta1):
        z1[x]=1
    else:
        z1[x]=0
print("z1: ",z1)

for x in range(4):

    yin2=(w12*x1[x])+(w22*x2[x])
    print("yin2 :", yin2)
    if(yin2>=theta2):
        z2[x]=1
    else:
        z2[x]=0
print("z2",z2)

for x in range(4):
    yin=w1*z1[x] + w2*z2[x]
    if(yin>=theta):
        z[x]=1
    else:
        z[x]=0

print("z: ",z)
if(z==y):
    print("XOR gate is recognized with given values")
else:
    print("Try again with different values")