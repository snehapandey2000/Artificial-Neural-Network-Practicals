def activationFun(value):
    if(value > 0):
        return 1
    else:
        return -1


def train(x, y, w, n):
    for i in range(n):
        for j in range(n):
            w[i][j] = w[i][j] + x[i]*y[j]
    return w


def test(x, w, n):
    y = []
    for j in range(n):
        temp = 0
        for i in range(n):
            temp += x[i]*w[i][j]
        y.append(temp)
    return y


def main():
    print("AutoAssociative TRAINING")
    rows = int(input("Enter number of inputs: "))
    n = int(input("Enter number of elements in input layer: "))
    w = w = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        w.append(temp)

    for i in range(rows):
        print("Enter input: ")
        x = input().strip().split(' ')
        x = list(int(a) for a in x)
        print("Enter output: ")
        y=[]
        for p in x:
            y.append(p)
        w = train(x, y, w, n)
        print("Updated Weights:")
        for a in range(n):
            for b in range(n):
                print(w[a][b], end=" ")
            print()
        print()

    print("AutoAssociative TESTING")

    t = int(input("Enter number of testing inputs: "))

    for i in range(t):
        print("Enter input: ")
        x = input().strip().split(" ")
        x = list(int(a) for a in x)

        y_in = test(x, w, n)
        print("Output for current Input: ")
        for j in range(len(y_in)):
            print(activationFun(y_in[j]), end=" ")

        print("\n")


main()