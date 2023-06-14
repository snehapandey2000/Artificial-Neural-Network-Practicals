x1 = [0,0,1,1]
x2 = [0,1,0,1]
y = [0,1,1,1]
z = [0,0,0,0]
yin=0



w1=int(input("Enter weight w1: "))
w2=int(input("Enter weight w2: "))
theta=int(input("Enter threshold value: "))
for x in range(4):
    yin=w1*x1[x] + w2*x2[x]
    if(yin>=theta):
        z[x]=1
    else:
        z[x]=0


if(z==y):
    print("OR gate is recognized with given values")
else:
    print("Try again with different values")