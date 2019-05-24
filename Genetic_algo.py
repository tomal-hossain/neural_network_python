import random,math
import matplotlib.pyplot as plt

chromosom = []
selected = []
avg = []
def InitialPopulation():
	global chromosom
	for i in range(0,10):
		new_chrom = []
		for j in range(0,5):
			locus = random.randrange(0,2)
			new_chrom.append(locus)
		new_chrom.append(0)
		new_chrom[5] = Fitness(new_chrom)
		chromosom.append(new_chrom)
def TotalFitness(Chrom):
	ftness = 0
	for val in Chrom:
		ftness += val[5]
	return ftness
def Fitness(Chrom):
	y = 0
	base = 1
	length = len(Chrom) - 2
	while length >= 0:
		if Chrom[length] == 1:
			y += base
		base = base*2
		length -= 1
	ftness = (-y*y/10)+3*y
	return ftness
def CrossOver(ChromX,ChromY):
	rnd1 = random.randrange(2,3)
	rnd2 = random.randrange(3,5)
	for i in range(rnd1,rnd2):
		temp = ChromX[i]
		ChromX[i] = ChromY[i]
		ChromY[i] = temp
	return ([ChromX,ChromY])
def Mutation(ChromX):
	rnd = random.randrange(2,5)
	if ChromX[rnd] == 0:
		ChromX[rnd] = 1
	else:
		ChromX[rnd] = 0
	ChromX[5] = Fitness(ChromX)
	return ChromX
def RoulateWheel(chromo):
	select = []
	Sorted = Sort(chromo)
	ftness = math.floor(TotalFitness(Sorted))
	length = len(Sorted)
	while len(select)<2:
		rnd = random.randrange(0,ftness)
		total = 0
		for j in range(0,length):
			total += Sorted[j][5]
			if total >= rnd:
				select.append(Sorted[j])
				break
			j += 1
	return select
	
def Sort(Chrom):
	temp = 0
	length = len(Chrom)
	for i in range(0,length):
		for j in range(i+1,length):
			if Chrom[i][5]>Chrom[j][5]:
				temp = Chrom[j]
				Chrom[j] = Chrom[i]
				Chrom[i] = temp
	return Chrom
InitialPopulation()
generation = []
for i in range(0,10):
	selected = []
	for j in range(0,5):
		select = []
		select = RoulateWheel(chromosom)
		sel = CrossOver(select[0],select[1])
		first = Mutation(sel[0])
		second = Mutation(sel[1])
		selected.append(first)
		selected.append(second)
	total = TotalFitness(selected)
	generation.append(i+1)
	avg.append(total/10)
	chromosom = []
	chromosom = selected
print(avg)
plt.plot(generation,avg,color='g')
plt.axis([0,12,0,30])
plt.xlabel('Generation')
plt.ylabel('Average Fitness')
plt.show()