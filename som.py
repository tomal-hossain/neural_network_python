from matplotlib import pyplot as plt
import random as rd
import math

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)

class Neuron:
	def __init__(self, center, weight):
		self.center = center
		self.weight = weight
		self.radius = 0.3
	def Update(self,new_weight):
		self.weight = new_weight

nodes = []
rgb = []
for i in range(0,25):
	r = rd.randrange(0,255)/255
	g = rd.randrange(0,255)/255
	b = rd.randrange(0,255)/255
	rgb.append((r,g,b))
nodes.append(Neuron((0.1,0.1),rgb[0]))
nodes.append(Neuron((0.3,0.1),rgb[1]))
nodes.append(Neuron((0.5,0.1),rgb[2]))
nodes.append(Neuron((0.7,0.1),rgb[3]))
nodes.append(Neuron((0.9,0.1),rgb[4]))
nodes.append(Neuron((0.1,0.3),rgb[5]))
nodes.append(Neuron((0.3,0.3),rgb[6]))
nodes.append(Neuron((0.5,0.3),rgb[7]))
nodes.append(Neuron((0.7,0.3),rgb[8]))
nodes.append(Neuron((0.9,0.3),rgb[9]))
nodes.append(Neuron((0.1,0.5),rgb[10]))
nodes.append(Neuron((0.3,0.5),rgb[11]))
nodes.append(Neuron((0.5,0.5),rgb[12]))
nodes.append(Neuron((0.7,0.5),rgb[13]))
nodes.append(Neuron((0.9,0.5),rgb[14]))
nodes.append(Neuron((0.1,0.7),rgb[15]))
nodes.append(Neuron((0.3,0.7),rgb[16]))
nodes.append(Neuron((0.5,0.7),rgb[17]))
nodes.append(Neuron((0.7,0.7),rgb[18]))
nodes.append(Neuron((0.9,0.7),rgb[19]))
nodes.append(Neuron((0.1,0.9),rgb[20]))
nodes.append(Neuron((0.3,0.9),rgb[21]))
nodes.append(Neuron((0.5,0.9),rgb[22]))
nodes.append(Neuron((0.7,0.9),rgb[23]))
nodes.append(Neuron((0.9,0.9),rgb[24]))

inputs = []
def InputNode():
	for i in range(0,10000):
		r = rd.randrange(0,255)/255
		g = rd.randrange(0,255)/255
		b = rd.randrange(0,255)/255
		inputs.append([r,g,b])
def EuclideanDist(x,y):
	dist = 0
	for i in range(0,len(x)):
		dist += pow(x[i]-y[i],2)
	dist = math.sqrt(dist)
	return dist
def FindBMU(inp):
	global nodes
	Min = EuclideanDist(inp,nodes[0].weight)
	BMU = nodes[0]
	for i in range(1,9):
		dist = EuclideanDist(inp,nodes[i].weight)
		if dist<Min:
			Min = dist
			BMU = nodes[i]
	return BMU

sigma = 0.5
influence = 0.6
learn_rate = 0.5
def UpdateNeuron():
	global nodes,inputs,sigma,influence,learn_rate
	InputNode()
	itration = 1
	for inp in inputs:
		BMU = FindBMU(inp)
		dist = EuclideanDist(BMU.weight,inp)
		time_const = 10000/(math.log(BMU.radius,0.001))
		sigma = sigma*math.exp(-itration/time_const)
		learn_rate = learn_rate * math.exp(-itration/time_const)
		influence = math.exp((-dist*dist)/(2*sigma*sigma))
		UpdatedValue = list(BMU.weight)
		UpdatedValue[0] = UpdatedValue[0] + influence*learn_rate*(inp[0]-UpdatedValue[0])
		UpdatedValue[1] = UpdatedValue[1] + influence*learn_rate*(inp[1]-UpdatedValue[1])
		UpdatedValue[2] = UpdatedValue[2] + influence*learn_rate*(inp[2]-UpdatedValue[2])
		BMU.Update(tuple(UpdatedValue))
		UpdateNeighbour(BMU)
		itration += 1
		print(influence)
def UpdateNeighbour(BMU):
	global nodes,radius,sigma,learn_rate
	for nd in nodes:
		inf = 0
		dist = EuclideanDist(nd.center,BMU.center)
		if 0<dist<=BMU.radius:
			inf = math.exp((-dist*dist)/(2*sigma*sigma))
			UpdatedValue = list(nd.weight)
			UpdatedValue[0] = UpdatedValue[0] + inf*learn_rate*(BMU.weight[0]-UpdatedValue[0])
			UpdatedValue[1] = UpdatedValue[1] + inf*learn_rate*(BMU.weight[1]-UpdatedValue[1])
			UpdatedValue[2] = UpdatedValue[2] + inf*learn_rate*(BMU.weight[2]-UpdatedValue[2])
			nd.Update(tuple(UpdatedValue))
			BMU.radius -= 0.007
	Draw()
def Draw():
	ax.clear()
	global nodes
	for nd in nodes:
		circ = plt.Circle(nd.center,0.1,color=nd.weight)
		ax.add_artist(circ)
	fig.canvas.draw()
	fig.canvas.flush_events()
UpdateNeuron()