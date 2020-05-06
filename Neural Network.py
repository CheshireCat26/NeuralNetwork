"""
    This document implement feed forward NN
"""

import math

class NeuralNetwork:
    def __init__(self, amount):
        """

        :param amount: amount of inputs
        """

        self.__size_input_layer = amount
        self.__hidden_layers = []
        self.__output_layer = None

    def add_hidden_layer(self, size):
        """
        must be used before add_output_layer

        :param size: number of neurons
        :return:
        """
        if self.__output_layer is not None:
            raise RuntimeError("After output_layer can't add more layers")

        if len(self.__hidden_layers) == 0:
            self.__hidden_layers.append(Layer(size, self.__size_input_layer))
        else:
            self.__hidden_layers.append(Layer(size,
                                              self.__hidden_layers[len(self.__hidden_layers) - 1].size()))

    def add_output_layer(self, size):
        """
        After it, you can't create new layers

        :param size: number of neurons
        :return:
        """

        if len(self.__hidden_layers) == 0:
            raise RuntimeError("You need at least 1 hidden layer")

        self.__output_layer = Layer(size, self.__hidden_layers[len(self.__hidden_layers) - 1].size())

    def amount_weights(self):
        """

        :return: len(get_all_weights)
        """

        amount = self.__output_layer.amount_weights()
        for hid_l in self.__hidden_layers:
            amount += hid_l.amount_weights()

        return amount

    def set_weights(self, weights):
        """

        :param weights: iterable
        :return:
        """

        indent = 0
        for hid_l in self.__hidden_layers:
            hid_l.set_weights(weights[indent:(indent + hid_l.amount_weights())])
            indent += hid_l.amount_weights()

        self.__output_layer.set_weights(weights[indent:])

    def get_output(self, m_input):
        """
        return answer from NN

        :param m_input: input for NN. len(input) == self.size_input_layer
        :return:
        """

        answer = 0
        for i, hid_l in enumerate(self.__hidden_layers):
            if i == 0:
                answer = hid_l.get_output(m_input)
            else:
                answer = hid_l.get_output(answer)

        return self.__output_layer.get_output(answer)


class Layer:
    def __init__(self, size, input_size):
        """

        :param size: number of neuron
        :param input_size: number of inputs of a neuron
        """

        self.__neurons = [Neuron(input_size) for _ in range(size)]
        self.__a_weights = size * input_size

    def amount_weights(self):
        """
        :return: numbers of weights in the layers
        """

        return self.__a_weights

    def set_weights(self, weights):
        """
        set weights to neuron in the layer

        :param weights: len(weights) must be equal to self.a_weights
        :return:
        """

        if len(weights) != self.__a_weights:
            raise RuntimeError("len(weights) != self.a_weights")

        intent = 0
        for neuron in self.__neurons:
            neuron.set_weights(weights[intent:(intent + neuron.size())])
            intent += neuron.size()

    def get_output(self, m_input):
        """

        :param m_input:
        :return: list of answers from neurons
        """

        answer = []
        for neuron in self.__neurons:
            answer.append(neuron.get_output(m_input))

        return answer

    def size(self):
        """

        :return: amount of neurons
        """

        return len(self.__neurons)


class Neuron:
    def __init__(self, size):
        """

        :param size: amount of inputs
        """

        self.__weight = []
        self.__input_size = size

    def set_weights(self, f_weights):
        """
        len(f_weights) == self.input_size

        :param f_weights: weight for neuron's inputs
        :return:
        """

        if len(f_weights) != self.__input_size:
            raise RuntimeError("len of f_weights must be == ti size of Neuron")

        self.__weight = f_weights

    def size(self):
        """

        :return: amount of inputs
        """

        return self.__input_size

    def get_output(self, f_input):
        """

        :param f_input: len(input) must be equal to  self.size()
        :return: answer from neuron
        """

        if len(f_input) != self.__input_size:
            raise RuntimeError("len(input)  != self.size()")

        x = sum([v * w for v, w in zip(f_input, self.__weight)])
        return math.exp(x) / (math.exp(x) + 1)


if __name__ == "__main__":
    NN = NeuralNetwork(2)
    NN.add_hidden_layer(100)
    NN.add_output_layer(1)
    weights = [0.01 for i in range(NN.amount_weights())]
    NN.set_weights(weights)

    print(NN.get_output([1, 1]))
