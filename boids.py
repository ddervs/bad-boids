from matplotlib import pyplot as plt
import random


class Boids(object):

    def __init__(self, boids, config):
        self.boids = boids
        self.config = config
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=self.config['x_plot_limits'], ylim=self.config['y_plot_limits'])
        self.scatter = self.ax.scatter(self.boids[0], self.boids[1])

    def fly_to_middle(self):
            xs, ys, xvs, yvs = self.boids
            for i in range(len(xs)):
                for j in range(len(xs)):
                    xvs[i] += (xs[j] - xs[i]) * self.config['move_to_middle_strength'] / len(xs)
                    yvs[i] += (ys[j] - ys[i]) * self.config['move_to_middle_strength'] / len(xs)
            self.boids = xs, ys, xvs, yvs

    def fly_away_nearby(self):
            xs, ys, xvs, yvs = self.boids
            for i in range(len(xs)):
                for j in range(len(xs)):
                    if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < self.config['alert_distance']:
                        xvs[i] += (xs[i] - xs[j])
                        yvs[i] += (ys[i] - ys[j])
            self.boids = xs, ys, xvs, yvs

    def match_speed(self):
            xs, ys, xvs, yvs = self.boids
            for i in range(len(xs)):
                for j in range(len(xs)):
                    if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < self.config['formation_flying_distance']:
                        xvs[i] += (xvs[j] - xvs[i]) * self.config['formation_flying_strength'] / len(xs)
                        yvs[i] += (yvs[j] - yvs[i]) * self.config['formation_flying_strength'] / len(xs)
            self.boids = xs, ys, xvs, yvs

    def move_boids(self):
            xs, ys, xvs, yvs = self.boids
            for i in range(len(xs)):
                xs[i] += xvs[i]
                ys[i] += yvs[i]
            self.boids = xs, ys, xvs, yvs

    def update_boids(self):

        self.fly_to_middle()
        self.fly_away_nearby()
        self.match_speed()
        self.move_boids()

    def animate(self, frame):
        self.update_boids()
        self.scatter.set_offsets(zip(self.boids[0], self.boids[1]))


def new_flock(count, xlimits, ylimits, vxlimits, vylimits):

    boids_x = [random.uniform(*xlimits) for x in range(count)]
    boids_y = [random.uniform(*ylimits) for x in range(count)]
    boid_x_velocities = [random.uniform(*vxlimits) for x in range(count)]
    boid_y_velocities = [random.uniform(*vylimits) for x in range(count)]
    return boids_x, boids_y, boid_x_velocities, boid_y_velocities
