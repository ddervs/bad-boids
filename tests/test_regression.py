import boids
from nose.tools import assert_almost_equal
import os
import yaml
from unittest import TestCase


class TestRegression(TestCase):

    def __init__(self, *args, **kwargs):

        super(TestRegression, self).__init__(*args, **kwargs)

    def test_bad_boids_regression(self):
        regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
        boid_data = regression_data["before"]
        test_boids = boids.Boids(boid_data)
        test_boids.update_boids()
        for after, before in zip(regression_data["after"], test_boids.boids):
            for after_value, before_value in zip(after, before):
                assert_almost_equal(after_value, before_value, delta=0.01)

