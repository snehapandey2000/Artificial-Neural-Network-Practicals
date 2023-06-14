import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = load_iris()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42)

# Define the neural network architecture
input_size = X_train.shape[1]  # Number of input features
hidden_size = 5  # Number of hidden units
output_size = len(np.unique(y_train))  # Number of output classes

# Randomly initialize the weights and biases
W1 = np.random.randn(input_size, hidden_size)
b1 = np.random.randn(hidden_size)
W2 = np.random.randn(hidden_size, output_size)
b2 = np.random.randn(output_size)

# Define the activation function (sigmoid)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the activation function (sigmoid)


def sigmoid_derivative(x):
    return x * (1 - x)


# Define the learning rate
learning_rate = 0.1

# Train the model using backpropagation
for i in range(10000):
    # Forward pass
    hidden_layer = sigmoid(np.dot(X_train, W1) + b1)
    output_layer = sigmoid(np.dot(hidden_layer, W2) + b2)

    # Compute the error
    error = y_train.reshape(-1, 1) - output_layer

    # Backward pass
    d_output = error * sigmoid_derivative(output_layer)
    d_hidden = np.dot(d_output, W2.T) * sigmoid_derivative(hidden_layer)

    # Update the weights and biases
    W2 += np.dot(hidden_layer.T, d_output) * learning_rate
    b2 += np.sum(d_output, axis=0) * learning_rate
    W1 += np.dot(X_train.T, d_hidden) * learning_rate
    b1 += np.sum(d_hidden, axis=0) * learning_rate

# Evaluate the model on the testing set
hidden_layer = sigmoid(np.dot(X_test, W1) + b1)
output_layer = sigmoid(np.dot(hidden_layer, W2) + b2)
predictions = np.argmax(output_layer, axis=1)
accuracy = np.mean(predictions == y_test)
print("Accuracy:", accuracy)
