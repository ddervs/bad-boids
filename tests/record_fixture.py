import yaml
import boids
from copy import deepcopy
import random

boids_data = boids.new_flock(50, (-450, 50.0), (300.0, 600.0), (0, 10.0), (-20.0, 20.0))
my_boids = boids.Boids(boids_data)

before = deepcopy(my_boids.boids)
my_boids.update_boids()
after = my_boids.boids
fixture = {"before": before, "after": after}
fixture_file = open("fixture.yml", 'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()
