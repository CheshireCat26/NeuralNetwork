My implementation of feed forward neural network

How to use:

NN = NeuralNetwork(amount_inputs) "Create instance of class. amount_inputs - number of neuronsin the input layer"

NN.add_hidden_layer(amount). "Add some hidden layers. You must have at lest one. amount - number of neurons in the layer."

"You have to add all hidden layers that you need at this point"

NN.add_output_layer(amount). "Add output layer. amount - number of neurons in the layer. You must have one and only one output layer."

"Here you can't add more hidden layers"

"You can't change NN dynamically"

NN.set_weights(weights) "Set all weights in NN. len(weights) must be == NN.amount_weights(). weights = value of all weights in NN"

NN.get_output(input) "Get output. "

"I use sigmoid as a activation function"

"Actually input layer doesn't exist. All what class save is it's size. So you must transfoms input values itself in apropriate form"
