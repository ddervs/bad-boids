import os

import yaml
from mock import patch
from numpy.testing import assert_array_almost_equal
from matplotlib import animation
import boids.boids.boids as boids
from nose.tools import assert_raises

config_filename = 'boids/config.yaml'
config = yaml.load(open(config_filename))


def test_boids_fixtures():
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
    boid_data = regression_data["reg_before"]
    test_boids = boids.Boids(boid_data, config)

    # Regression test
    test_boids.update_boids()
    for after, before in zip(regression_data["reg_after"], test_boids.boids):
        assert_array_almost_equal(after, before, 2)

    # Test sub_functions
    test_boids.fly_to_middle()
    for after, before in zip(regression_data["fly_to_middle"], test_boids.boids):
        assert_array_almost_equal(after, before, 2)

    test_boids.fly_away_nearby()
    for after, before in zip(regression_data["fly_away_nearby"], test_boids.boids):
        assert_array_almost_equal(after, before, 2)

    test_boids.match_speed()
    for after, before in zip(regression_data["match_speed"], test_boids.boids):
        assert_array_almost_equal(after, before, 2)

    test_boids.move_boids()
    for after, before in zip(regression_data["move_boids"], test_boids.boids):
        assert_array_almost_equal(after, before, 2)


def test_new_flock():
    num_boids = 20
    boids_range = [-100, 100]
    test_boids = boids.new_flock(num_boids, boids_range, boids_range, boids_range, boids_range)

    for array in test_boids:
        # Check right number of boids
        assert cmp(array.shape, (num_boids, 2)) == 0
        # Check boids positions and velocities in range
        in_range = boids_range[0] < array.all() < boids_range[1]
        assert in_range


@patch.object(boids.Boids, 'update_boids')
def test_animate(mock_update_boids):
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
    boid_data = regression_data["reg_before"]
    test_boids = boids.Boids(boid_data, config)
    # Test that animation calls update_boids method
    frame = None
    test_boids.animate(frame)
    assert mock_update_boids.called


@patch.object(animation, 'FuncAnimation')
def test_run_animation(mock_FuncAnimation):
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
    boid_data = regression_data["reg_before"]
    test_boids = boids.Boids(boid_data, config)
    # Test that run_animation calls FuncAnimation
    test_boids.run_animation()
    assert mock_FuncAnimation.called


def test_init():
    # Test that appropriate exceptions raised if incorrect types passed
    some_list = [1, 2, 3]
    assert_raises(TypeError, boids.Boids, some_list, dict(key=some_list))
    assert_raises(TypeError, boids.Boids, (some_list, some_list), some_list)
