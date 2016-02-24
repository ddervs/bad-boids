import boids
from nose.tools import assert_almost_equal
import os
import yaml


def test_boids_fixtures():

    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
    boid_data = regression_data["reg_before"]
    test_boids = boids.Boids(boid_data)

    # Regression test
    test_boids.update_boids()
    for after, before in zip(regression_data["reg_after"], test_boids.boids):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)
            
    # Test sub_functions
    test_boids.fly_to_middle()
    for after, before in zip(regression_data["fly_to_middle"], test_boids.boids):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)

    test_boids.fly_away_nearby()
    for after, before in zip(regression_data["fly_away_nearby"], test_boids.boids):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)

    test_boids.match_speed()
    for after, before in zip(regression_data["match_speed"], test_boids.boids):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)

    test_boids.move_boids()
    for after, before in zip(regression_data["move_boids"], test_boids.boids):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)
