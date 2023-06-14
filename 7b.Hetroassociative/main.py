def activationFunction(value):
    if value > 0:
        return 1
    elif value == 0:
        return 0
    else:
        return -1


def trainingalgo(x, y, w, n, m):
    for i in range(n):
        for j in range(m):
            w[i][j] += x[i]*y[j]

    return w


def testingalgo(x, w, n, m):
    y = []
    for j in range(m):
        temp = 0
        for i in range(n):
            print(w[i][j])
            temp += x[i]*w[i][j]
        y.append(temp)
    return y


def main():
    print("--------* Training Begins *--------")
    rows = int(input("Enter number of inputs: "))
    n = int(input("Enter number of in input neurons: "))
    m = int(input("Enter number of elements in output neurons: "))
    w = [[0 for i in range(m)] for i in range(n)]

    for i in range(rows):
        print(f"Enter input s{i}: ")
        x = input().strip().split(' ')
        x = list(int(a) for a in x)

        print(f"Enter output t{i}: ")
        y = input().strip().split(' ')
        y = list(int(a) for a in y)

        w = trainingalgo(x, y, w, n, m)
        print("Updated Weights:")

        for a in range(n):
            for b in range(m):
                print(w[a][b], end=" ")
            print("\n")

    print("--------* Testing Begins *-----")

    t = int(input("Enter number of testing inputs: "))

    for i in range(t):
        print("Enter input: ")
        x = input().strip().split(" ")
        x = list(int(a) for a in x)

        y_in = testingalgo(x, w, n, m)
        print("Output for current Input: ")
        for j in range(len(y_in)):
            print(activationFunction(y_in[j]), end=" ")
        print("\n")


main()