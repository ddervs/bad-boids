import yaml
import boids
from copy import deepcopy
import os

os.chdir(os.path.pardir)

boids_data = boids.new_flock(50, (-450, 50.0), (300.0, 600.0), (0, 10.0), (-20.0, 20.0))
my_boids = boids.Boids(boids_data)

# Regression Test
reg_before = deepcopy(my_boids.boids)
my_boids.update_boids()
reg_after = deepcopy(my_boids.boids)

# update_boids sub functions
my_boids.fly_to_middle()
fly_to_middle = deepcopy(my_boids.boids)
my_boids.fly_away_nearby()
fly_away_nearby = deepcopy(my_boids.boids)
my_boids.match_speed()
match_speed = deepcopy(my_boids.boids)
my_boids.move_boids()
move_boids = deepcopy(my_boids.boids)

fixture = dict(reg_before=reg_before,
               reg_after=reg_after,
               fly_to_middle=fly_to_middle,
               fly_away_nearby=fly_away_nearby,
               match_speed=match_speed,
               move_boids=move_boids
               )

os.chdir('tests')
fixture_file = open("fixture.yml", 'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()
