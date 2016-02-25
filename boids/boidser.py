import boids
import yaml
from matplotlib import animation
from matplotlib import pyplot as plt
import os


def make_boids(config_filename):
    """
    :param config_filename: config filename
    :return:
    """
    default_config_name = os.path.dirname(os.path.realpath(__file__))[:-5] + 'config.yaml'
    default_config = yaml.load(open(default_config_name))
    input_config = yaml.load(open(config_filename))
    for key, value in default_config.items():
        if key in input_config:
            default_config[key] = input_config[key]
            
    boids_data = boids.new_flock(default_config['number_of_boids'], default_config['x_initial'],
                                 default_config['vx_initial'], default_config['y_initial'],
                                 default_config['vy_initial'])

    my_boids = boids.Boids(boids_data, default_config)

    anim = animation.FuncAnimation(my_boids.fig, my_boids.animate,
                                   frames=default_config['frames'], interval=default_config['interval'])
    plt.show()
