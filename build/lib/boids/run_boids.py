import yaml
from matplotlib import pyplot as plt

import boids

config_filename = 'config.yaml'
config = yaml.load(open(config_filename))

boids_data = boids.new_flock(config['number_of_boids'], config['x_initial'], config['y_initial'], config['vx_initial'],
                             config['vy_initial'])
my_boids = boids.Boids(boids_data, config)

ani = my_boids.run_animation()
plt.show()
