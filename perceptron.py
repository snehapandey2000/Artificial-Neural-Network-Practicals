import numpy as np


def sigmoid(x):
    return 1/(1+np.exp(-x))


def activation_sigmoid(x):
    y = sigmoid(x)
    if y > 0:
        return 1
    elif y == 0:
        return 0
    else:
        return -1


def step_function(y):
    if y > 0:
        return 1
    elif y == 0:
        return 0
    else:
        return -1


w = [0, 0]
Wold = [0, 0]
b = 0
alpha = 1

x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
t = [1, -1, -1, -1]
epoch = True
num = 1
while(epoch):
    print("\n Epoch", num, " : ")
    num = num+1
    print("_______________________________________")
    for i in range(4):
        yin = x1[i]*w[0]+x2[i]*w[1]+b
        y = step_function(yin)
        print("y:", y)
        if(y != t[i]):
            print("Weights Updated")
            w[0] = w[0] + alpha*t[i]*x1[i]
            w[1] = w[1] + alpha*t[i]*x2[i]
            b = b + alpha*t[i]

        print(f'Weights : w1 = {w[0]} , w2 = {w[1]} , b = {b}')
    if(Wold[0] == w[0] and Wold[1] == w[1]):
        epoch = 0
    Wold = w

print(f'Weights : w1 = {w[0]} , w2 = {w[1]} , b = {b}')
