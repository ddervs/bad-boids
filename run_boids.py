import boids
from matplotlib import pyplot as plt
from matplotlib import animation

boids_data = boids.new_flock(50, (-450, 50.0), (300.0, 600.0), (0, 10.0), (-20.0, 20.0))
my_boids = boids.Boids(boids_data)

anim = animation.FuncAnimation(my_boids.fig, my_boids.animate,
                               frames=50, interval=50)
plt.show()
