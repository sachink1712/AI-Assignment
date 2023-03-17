# Projectile motion simulation.
from matplotlib import pyplot as pp
import math

def updatePosition(initialposition,initialspeed,acceleration,time):
    newposition = initialposition+initialspeed*time+.5*acceleration*time**2
    return newposition

g = 4.905 #gravity at Earth's surface
x0 = 0  #initial x position, m
y0 = 10 #inital height, m
acceleration_x = 0
acceleration_y = -g

#muzzle velocity, m/s
v0 = 20
launchAngle =50

v0_x = v0 * math.cos(math.radians(launchAngle))
v0_y = v0 * math.sin(math.radians(launchAngle))

x = [x0]
y = [y0]
time = [0] #list for storing the elapsed time
dt = 0.1 #time step

##### You should not have to modify code above this point to make the code work.
##### But, you can change things above if you trying to simulate different
##### initial conditions.

#Add a loop below. Include an update to the x, y, and time variables.
#The x update is done for you.

#Each time through the loop, you should append the elapsed time
#to the 'time' variable by adding dt to the last elapsed time value
while y[-1] >= 0:
    # Update x, y, and time variables
    x.append(updatePosition(x0, v0_x, acceleration_x, time[-1] + dt))
    y.append(updatePosition(y0, v0_y, acceleration_y, time[-1] + dt))
    time.append(time[-1] + dt)
print(x[-1])

#plot the projectile!
pp.plot(x,y)
pp.xlabel('x (m)')
pp.ylabel('height (m)')
pp.savefig('plot.png')
