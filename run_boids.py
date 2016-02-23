import boids
from matplotlib import pyplot as plt
import random
from matplotlib import animation

boids_x = [random.uniform(-450, 50.0) for x in range(50)]
boids_y = [random.uniform(300.0, 600.0) for x in range(50)]
boid_x_velocities = [random.uniform(0, 10.0) for x in range(50)]
boid_y_velocities = [random.uniform(-20.0, 20.0) for x in range(50)]
input_boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)

my_boids = boids.Boids(input_boids)
anim = animation.FuncAnimation(my_boids.fig, my_boids.animate,
                               frames=50, interval=50)
plt.show()
