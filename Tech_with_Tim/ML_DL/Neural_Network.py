import numpy as np
import matplotlib.pyplot as plt


class Neuron:

    def __init__(self, weights=[], bias=0):
        self.weights = weights
        self.bias = bias

    def __str__(self):
        return f"weights: {self.weights}\nbias: {self.bias}"

    def sigmoid(Z):
        return 1 / (1 + np.exp(-Z))

    def initialize_parameters(self, dim):
        self.weights = np.zeros(dim, 1)
        self.bias = 0

    def update_parameters(self, dw, db, learning_rate):
        self.weights = self.weights - learning_rate * dw
        self.bias = self.bias - learning_rate * db

    def compute_cost(self, AL, Y):
        m = Y.shape[1]
        cost = (1 / m) * np.sum(-1 * (Y * np.log(AL) + (1 - Y) * np.log(1 - AL)))
        cost = np.squeeze(cost)
        return cost

    def forward(self, X):
        Z = np.dot(self.weights.T, X) + self.bias
        AL = Neuron.sigmoid(Z)
        return AL

    def backward(self, AL, X, Y):
        m = X.shape[1]
        dZ = AL - Y
        dw = (1 / m) * np.dot(X, dZ.T)
        db = (1 / m) * np.sum(dZ)
        return (dw, db)

    def model_logistic_fit(self, X, Y, num_iterations=2000, learning_rate=0.005, print_cost=False):
        Neuron.initialize_parameters(self, X.shape[0])

        costs = []
        for i in range(0, num_iterations):
            AL = Neuron.forward(self, X)
            cost = Neuron.compute_cost(self, AL, Y)

            dw, db = Neuron.backward(self, AL, X, Y)

            Neuron.update_parameters(self, dw, db, learning_rate)

            if print_cost and i % 100 == 0:
                print("Cost after iteration %i: %f" % (i, cost))
                costs.append(cost)

        plt.plot(np.squeeze(costs))
        plt.ylabel('cost')
        plt.xlabel('iterations (per hundreds)')
        plt.title("Learning rate =" + str(learning_rate))
        plt.show()

    def accuracy(self, prediction, Y):
        count = 0
        for i in range(Y.shape[1]):
            if prediction[0][i] == Y[0][i]:
                count += 1

        acc = count * 100 / Y.shape[1]
        print("Accuracy: {}".format(acc))
        return acc

    def predict(self, X, threshold = 0.5, give_probability = False):
        predictions = Neuron.forward(self, X)
        if not give_probability:
            predictions[predictions > threshold] = 1
            predictions[predictions <= threshold] = 0
        return predictions


class Layer_of_Neurons:

    def __init__(self, num, Weights, Biases):
        self.layer = []
        self.num = num
        self.Weights = Weights
        self.Biases = Biases
        self.grad = {}
        self.Z = []
        for i in range(num):
            self.layer.append(Neuron(Weights[i], Biases[i]))

    def __str__(self):
        return f"Weights: {self.Weights}\nBiases: {self.Biases}\nNo. of Neurons: {self.num}"

    def Activation(self, z, act):
        zero = z
        if act == 'relu':
            zero[zero <= 0] = 0
            return zero
        if act == 'sigmoid':
            return 1 / (1 + np.exp(-z))

    def Back_Activation(self, act):
        x = self.Z
        if act == 'relu':
            x[x <= 0] = 0
            x[x > 0] = 1
        if act == 'sigmoid':
            x = Layer_of_Neurons.Activation(self, x, act='sigmoid') * (
                        1 - Layer_of_Neurons.Activation(self, x, act='sigmoid'))
        return x

    def Forward_prop(self, Aprev, act):
        self.Z = np.dot(self.Weights, Aprev) + self.Biases
        self.A = Layer_of_Neurons.Activation(self, self.Z, act)
        return self.A

    def Backward_prop(self, dA, Aprev, act):
        m = Aprev.shape[1]
        self.dZ = dA * Layer_of_Neurons.Back_Activation(self, act)
        self.dAprev = np.dot(self.Weights.T, self.dZ)
        self.dW = (1 / m) * np.dot(self.dZ, Aprev.T)
        self.db = (1 / m) * np.sum(self.dZ, axis=1, keepdims=True)

        return self.dAprev, self.dW, self.db


class Neural_Network:

    def __init__(self, L, layer_dims):
        self.neural_network = []
        self.L = L
        self.layer_dims = layer_dims
        self.parameters = Neural_Network.initialize_parameters_deep(self)
        self.grads = {}
        self.predictions = []
        for i in range(1, L + 1):
            self.neural_network.append(
                Layer_of_Neurons(self.layer_dims[i], self.parameters['W' + str(i)], self.parameters['b' + str(i)]))

    def __str__(self):
        return f"No. of Layers: {self.L}\nThe Layer Dimensions: {self.layer_dims}\nThe Parameters: {self.parameters}"

    def compute_cost(self, AL, Y):
        m = Y.shape[1]
        cost = - (1 / m) * np.sum(Y * np.log(AL) + (1 - Y) * np.log(1 - AL))
        cost = np.squeeze(cost)
        return cost

    def initialize_parameters_deep(self):
        parameters = {}
        L = len(self.layer_dims)

        for l in range(1, L):
            parameters['W' + str(l)] = np.random.randn(self.layer_dims[l], self.layer_dims[l - 1]) * 0.01
            parameters['b' + str(l)] = np.zeros((self.layer_dims[l], 1))

        return parameters

    def update_parameters(self, learning_rate):

        for l in range(self.L):
            self.parameters["W" + str(l + 1)] = self.parameters["W" + str(l + 1)] - learning_rate * self.grads[
                "dW" + str(l + 1)]
            self.parameters["b" + str(l + 1)] = self.parameters["b" + str(l + 1)] - learning_rate * self.grads[
                "db" + str(l + 1)]
            self.neural_network[l].Weights = self.parameters["W" + str(l + 1)]
            self.neural_network[l].Biases = self.parameters["b" + str(l + 1)]

    def Forward_Propagation(self, X):
        A = X
        for i in range(1, self.L):
            Aprev = A
            A = self.neural_network[i - 1].Forward_prop(Aprev, act="relu")

        AL = self.neural_network[self.L - 1].Forward_prop(A, act="sigmoid")
        return AL

    def Backward_Propagation(self, AL, X, Y):
        dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))

        dA, self.grads['dW' + str(self.L)], self.grads['db' + str(self.L)] = self.neural_network[self.L - 1].Backward_prop(dAL, self.neural_network[self.L - 2].A, act='sigmoid')
        for i in range(self.L - 1, 1, -1):
            dA, self.grads['dW' + str(i)], self.grads['db' + str(i)] = self.neural_network[i - 1].Backward_prop(dA, self.neural_network[i - 2].A, act='relu')

        dA, self.grads['dW' + str(1)], self.grads['db' + str(1)] = self.neural_network[0].Backward_prop(dA, X, act='relu')

    def model_fit(self, X, Y, num_iterations=2000, learning_rate=0.005, print_cost=False):

        costs = []
        for i in range(0, num_iterations):
            AL = Neural_Network.Forward_Propagation(self, X)
            cost = Neural_Network.compute_cost(self, AL, Y)

            Neural_Network.Backward_Propagation(self, AL, X, Y)

            Neural_Network.update_parameters(self, learning_rate)

            if print_cost and i % 100 == 0:
                print(f"Cost after iteration {i:d}: {cost:f}")
                costs.append(cost)

        plt.plot(np.squeeze(costs))
        plt.ylabel('cost')
        plt.xlabel('iterations (per hundreds)')
        plt.title("Learning rate =" + str(learning_rate))
        plt.show()

    def accuracy(self, Y):
        count = 0
        for i in range(Y.shape[1]):
            if (self.predictions.T[i] == Y.T[i]).all():
                count += 1

        acc = count * 100 / Y.shape[1]
        print("Accuracy: {}".format(acc))
        return acc

    def predict(self, X, threshold=0.5, give_probability=False):

        A = X
        for i in range(1, self.L):
            Aprev = A
            A = self.neural_network[i - 1].Forward_prop(Aprev, act="relu")

        self.predictions = self.neural_network[self.L - 1].Forward_prop(A, act="sigmoid")

        if not give_probability:
            # Convert predictions to binary values
            if self.layer_dims[-1] > 1:
                # Converting the predictions to binary values for many O/P neurons
                self.predictions = self.predictions.T
                predict_bin = np.zeros_like(self.predictions)
                predict_bin[np.arange(len(self.predictions)), self.predictions.argmax(1)] = 1
                self.predictions = predict_bin
                self.predictions = self.predictions.T
            else:
                # Converting the predictions to binary values using a threshold value for one O/P neuron
                self.predictions[self.predictions > threshold] = 1
                self.predictions[self.predictions <= threshold] = 0

        return self.predictions


