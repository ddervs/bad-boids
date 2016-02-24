import boids
from matplotlib import pyplot as plt
from matplotlib import animation
import yaml

config_filename = 'config.yaml'
config = yaml.load(open(config_filename))

boids_data = boids.new_flock(config['number_of_boids'], config['x_initial'], config['y_initial'], config['vx_initial'],
                             config['vy_initial'])
my_boids = boids.Boids(boids_data, config)

anim = animation.FuncAnimation(my_boids.fig, my_boids.animate,
                               frames=50, interval=50)
plt.show()
