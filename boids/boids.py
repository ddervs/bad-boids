from matplotlib import pyplot as plt
import numpy as np


class Boids(object):

    def __init__(self, boids, config):
        self.boids = boids
        self.config = config
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=self.config['x_plot_limits'], ylim=self.config['y_plot_limits'])
        self.scatter = self.ax.scatter(self.boids[0][:], self.boids[1][:])

    def fly_to_middle(self):

        positions, velocities = self.boids
        middle = np.mean(positions, 0)
        direction_to_middle = positions - middle
        velocities -= direction_to_middle * self.config['move_to_middle_strength']
        positions += velocities
        self.boids = positions, velocities

    def fly_away_nearby(self):

        positions, velocities = self.boids

        # 50x50x2 array of positional separations
        separations = positions[np.newaxis, :, :] - positions[:, np.newaxis, :]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 2)

        close_birds = square_distances < self.config['alert_distance']
        separations_if_close = np.copy(separations)
        far_away = np.logical_not(close_birds)
        separations_if_close[:, :, 0][far_away] = 0
        separations_if_close[:, :, 1][far_away] = 0

        velocities = velocities + np.sum(separations_if_close, 1)
        self.boids = positions, velocities

    def match_speed(self):

        positions, velocities = self.boids

        # 50x50x2 array of positional separations
        separations = positions[np.newaxis, :, :] - positions[:, np.newaxis, :]
        squared_displacements = separations * separations
        square_distances = np.sum(squared_displacements, 2)

        # 50x50x2 array of velocity separations
        velocity_differences = velocities[np.newaxis, :, :] - velocities[:, np.newaxis, :]
        very_far = square_distances > self.config['formation_flying_distance']
        velocity_differences_if_close = np.copy(velocity_differences)
        velocity_differences_if_close[:, :, 0][very_far] = 0
        velocity_differences_if_close[:, :, 1][very_far] = 0
        velocities -= np.mean(velocity_differences_if_close, 0) * self.config['formation_flying_strength']

        self.boids = positions, velocities

    def move_boids(self):

        positions, velocities = self.boids
        positions += velocities
        self.boids = positions, velocities

    def update_boids(self):

        self.fly_to_middle()
        self.fly_away_nearby()
        self.match_speed()
        self.move_boids()

    def animate(self, frame):
        self.update_boids()
        self.scatter.set_offsets(zip(self.boids[0][:], self.boids[0][:]))


def new_flock(count, xlimits, ylimits, vxlimits, vylimits):

    def rand_from_limits(limits):
        return limits[0] + np.random.rand(count) * (limits[1] - limits[0])

    boids_x = rand_from_limits(xlimits)
    boids_y = rand_from_limits(ylimits)
    boids_vx = rand_from_limits(vxlimits)
    boids_vy = rand_from_limits(vylimits)

    positions = np.column_stack((boids_x, boids_y))
    velocities = np.column_stack((boids_vx, boids_vy))

    return positions, velocities
