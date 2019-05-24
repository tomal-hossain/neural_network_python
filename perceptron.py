import random,math,time
import matplotlib.pyplot as plt
import matplotlib.pyplot as pt
from matplotlib.lines import Line2D


plt.ion()
fig = plt.figure(1)
ax = fig.add_subplot(111)
points = []
error = []
iteration = []
class Perceptron:
	def __init__(self,pos,category,color):
		self.pos = pos
		self.category = category
		self.color = color

def RandomPoint():
	global points
	for i in range(0,50):
		x = random.uniform(0.3,1.0)
		y = random.uniform(0.5,1.0)
		category = 1
		points.append(Perceptron((x,y),category,'green'))
	for i in range(0,50):
		x = random.uniform(0.0,0.5)
		y = random.uniform(0.0,0.5)
		category = 0
		points.append(Perceptron((x,y),category,'red'))
def CheckPosition(p,q):
	global a,b,c
	pos = a*p+b*q-c
	if(pos>0):
		return 'right'
	else:
		return 'left'
def Distance(p,q):
	global a,b,c
	pos = a*p+b*q-c
	return (1/(1+math.exp(pos)))
def Draw(line,select):
	global points
	ax.clear()
	for p in points:
		if select==p:
			pnt = plt.Circle(p.pos,0.01,color='blue')
		else:
			pnt = plt.Circle(p.pos,0.005,color=p.color)
		ax.add_artist(pnt)
	line_x,line_y = zip(line)
	ax.add_line(Line2D(line_x,line_y,linewidth=1,color='blue'))
	fig.canvas.draw()
	fig.canvas.flush_events()
	#time.sleep(1)
def EditLine():
	global points,a,b,c,error
	learn = 0.08
	for i in range(0,100):
		p = random.randrange(0,100)
		select = points[p]
		selected_x = select.pos[0]
		selected_y = select.pos[1]
		region = CheckPosition(selected_x,selected_y)
		target = select.category
		compute = Distance(selected_x,selected_y)
		if (select.category == 0 and region=='right') or (select.category == 1 and region=='left'):
			a = a + learn*(target-compute)
			b = b + learn*(target-compute)
			c = c - learn*(target-compute)
		er = 0
		for p in points:
			reg = CheckPosition(p.pos[0],p.pos[1])
			if (p.category == 0 and reg=='right') or (p.category == 1 and reg=='left'):
				er += Distance(p.pos[0],p.pos[1])
		error.append(er)
		iteration.append(i+1)
		line = [(c/a,0),(0,c/b)]
		Draw(line,select)
RandomPoint()
a = random.uniform(0.7,1)
b = random.uniform(0.7,1)
c = random.uniform(0.1,0.3)
EditLine()
plt.ioff()
plt.close(1)
pt.figure(2)
pt.plot(iteration,error,color='g')
pt.title("Error Calculation")
pt.axis([0,100,0,30])
pt.xlabel('Iteration')
pt.ylabel('Error')
pt.show()