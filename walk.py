import random
from matplotlib import pyplot as pp

distanceTraveled = [0]
nMax = 1000
n = 0


### The code in the lines below need to be in a loop of some sort
for i in range(nMax):
    nextStep = random.randint(-1,1)
    distanceTraveled.append(distanceTraveled[-1]+nextStep)
    n += 1
print(distanceTraveled)
###

#Plot the random walk
pp.plot(distanceTraveled)
pp.xlabel('Step number')
pp.ylabel('Distance from the start')
pp.title('A Random Walk')
pp.savefig('plot.png')
