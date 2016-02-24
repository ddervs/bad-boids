import boids
from nose.tools import assert_almost_equal
import os
import yaml
from mock import patch

config_filename = 'config.yaml'
config = yaml.load(open(config_filename))


def test_boids_fixtures():
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
    boid_data = regression_data["reg_before"]
    test_boids = boids.Boids(boid_data, config)

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


def test_new_flock():
    num_boids = 20
    boids_range = (-100, 100)
    test_boids = boids.new_flock(num_boids, boids_range, boids_range, boids_range, boids_range)

    for boid_list in test_boids:
        # Check right number of boids
        assert (len(boid_list) == num_boids)
        # Check boids positions and velocities in range
        for boid in boid_list:
            min_boid, max_boid = boids_range
            assert (min_boid <= boid <= max_boid)


@patch.object(boids.Boids, 'update_boids')
def test_animate(mock_update_boids):
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
    boid_data = regression_data["reg_before"]
    test_boids = boids.Boids(boid_data, config)
    # Test that animation calls update_boids method
    frame = None
    test_boids.animate(frame)
    assert mock_update_boids.called
