import math,random
import matplotlib.pyplot as plt
import numpy as np

Input = []
Target = []
HiddenNode = []
OutNode = None
learn = 0.8
class  Node:
	def __init__(self, weight):
		self.weight = weight
		self.netVal = 0
		self.outVal = 0
def Sample():
	global sample,HiddenNode,OutNode
	for i in range(0,10):
		x = random.randrange(0,2)
		y = random.randrange(0,2)
		Input.append([x,y])
		t = random.uniform(0,1)
		Target.append(t)
	for i in range(0,3):
		w1 = random.uniform(0,1)
		w2 = random.uniform(0,1)
		HiddenNode.append(Node([w1,w2]))
	w1 = random.uniform(0,1)
	w2 = random.uniform(0,1)
	w3 = random.uniform(0,1)
	OutNode = Node([w1,w2,w3])
def DotProduct(mat1,mat2):
	return np.dot(mat1,mat2)
def Sigmoid(x):
	return (1.0/(1+math.exp(-x)))
def InputToHidden(inp):
	global HiddenNode
	for node in HiddenNode:
		node.netVal = DotProduct(node.weight,inp)
		node.outVal = Sigmoid(node.netVal)
def HiddenToOutput():
	global OutNode,HiddenNode
	X = []
	for node in HiddenNode:
		X.append(node.outVal)
	OutNode.netVal = DotProduct(OutNode.weight,X)
	OutNode.outVal = Sigmoid(OutNode.netVal)
def OutputToHidden(tar):
	global OutNode,learn
	newWeight = []
	weight = OutNode.weight
	out = OutNode.outVal
	for w in weight:
		delW = - (tar - out)*out*(1-out)*w
		w = w - learn*delW
		newWeight.append(w)
	OutNode.weight = newWeight
def HiddenToInput(tar,inp):
	global HiddenNode,OutNode
	out = OutNode.outVal
	i=0
	for node in HiddenNode:
		weightHtoOut = OutNode.weight[i]
		j = 0
		newWeight = []
		for w in node.weight:
			delOutH = - (tar - out)*out*(1-out)*weightHtoOut
			delNetH = node.outVal*(1-node.outVal)
			delW = delOutH*delNetH*inp[j]
			w = w - learn*delW
			newWeight.append(w)
			j += 1
		node.weight = newWeight
		i += 1
def ErrorCalculate(tar,out):
	return 0.5*(tar-out)**2
Sample()
error = []
epoch = []
for k in range(1,50):
	i = 0;
	err = 0
	for val in Input:
		InputToHidden(Input[i])
		HiddenToOutput()
		e = ErrorCalculate(Target[i],OutNode.outVal)
		err += e
		OutputToHidden(Target[i])
		HiddenToInput(Target[i],val)
		i += 1
	print(err)
	error.append(err)
	epoch.append(k)
plt.plot(epoch,error,color='g')
plt.axis([0,50,0,1])
plt.xlabel('Epoch')
plt.ylabel('Error')
plt.show()