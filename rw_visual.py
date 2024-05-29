import matplotlib.pyplot as plt 

from random_walk import RandomWalk 

# Make a random walk
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the random walk
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
