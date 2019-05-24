import math
import random
from matplotlib import pyplot as plt
import time

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)

points=[]
center =[]
cluster = [[],[],[]]

def MinDistance(x,y):
	global center
	pos=-1
	dist = 9999999.0
	for i in range(0,3):
		new_dist = math.sqrt( (pow(center[i][0]-x,2)) + (pow(center[i][1]-y,2)) )
		if dist > new_dist :
			dist = new_dist
			pos = i
	return pos
def UpdateCenter(i,x_mean,y_mean):
	global center
	if (math.fabs(center[i][0]-x_mean)<=0.01) and (math.fabs(center[i][1]-y_mean)<=0.01):
		return 0
	else:
		return 1
diff_x = 0
diff_x = 50
for i in range(0,300):
	if i<100:
		x=random.randrange(0,40)/100
		y=random.randrange(0,40)/100
	elif 100<i<200:
		x=random.randrange(60,100)/100
		y=random.randrange(0,40)/100
	else:
		x=random.randrange(30,70)/100
		y=random.randrange(60,100)/100
	points.append([x,y])
for i in range(0,3):
	x=random.randrange(1,100)/100
	y=random.randrange(1,100)/100
	center.append([x,y])
color = ['green','red','blue']
def Show():
	ax.clear()
	i=0
	for val in cluster:
		for c in val:
			cir = plt.scatter(c[0],c[1],s=20,marker='*',color=color[i])
			ax.add_artist(cir)
		c_x = center[i][0]
		c_y = center[i][1]
		cir2 =plt.Circle((c_x,c_y),0.02,color=color[i])
		ax.add_artist(cir2)
		i += 1	
	plt.xlabel('Iteration')
	fig.canvas.draw()
	if update ==1:
		fig.canvas.flush_events()
	time.sleep(1)
update = 1
def Main():
	global points,cluster,center,update
	while update:	
		for p in points:
			pos = MinDistance(p[0],p[1])
			cluster[pos].append(p)
		x_mean = 0
		y_mean = 0
		i = 0
		update = 0
		for val in cluster:
			x_sum = 0
			y_sum = 0
			j = 0
			for p in val:
				x_sum += p[0]
				y_sum += p[1]
				j += 1
			x_mean = x_sum / j
			y_mean = y_sum / j
			up = UpdateCenter(i,x_mean,y_mean)
			if up == 1:
				center[i] = [x_mean,y_mean]
				update = 1
				Show()
			i += 1
		if update == 1:
			cluster = [[],[],[]]
Main()