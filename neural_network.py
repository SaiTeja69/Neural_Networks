import numpy as np
class NeuralNetwork:
	def __init__(self,input,y):
		self.input=input
		self.weights1=np.random.rand(self.input.shape[1],4)
		self.weights2=np.random.rand(1,4)
		self.y=y
		self.output=np.zeroes(y.shape)
	def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))
    