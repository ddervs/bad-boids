from argparse import ArgumentParser
from boidser import make_boids
import os

default_config_file_name = os.path.dirname(os.path.realpath(__file__))[:-5] + 'config.yaml'

def process():
    parser = ArgumentParser(description='Runs the boids simulation.')
    parser.add_argument('--config', default=default_config_file_name,
                        help='YAML file with simulation options. See README.md for specification.')
    arguments = parser.parse_args()

    make_boids(arguments.config)


if __name__ == "__main__":
    process()
