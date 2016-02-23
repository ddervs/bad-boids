import yaml
import boids
from copy import deepcopy
import random

boids_x = [random.uniform(-450, 50.0) for x in range(50)]
boids_y = [random.uniform(300.0, 600.0) for x in range(50)]
boid_x_velocities = [random.uniform(0, 10.0) for x in range(50)]
boid_y_velocities = [random.uniform(-20.0, 20.0) for x in range(50)]
input_boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)

my_boids = boids.Boids(input_boids)

before = deepcopy(my_boids.boids)
my_boids.update_boids()
after = my_boids.boids
fixture = {"before": before, "after": after}
fixture_file = open("fixture.yml", 'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()
