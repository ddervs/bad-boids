from matplotlib import pyplot as plt
import random

class Boids(object):

    def __init__(self, boids, x_limits=(-500, 1500), y_limits=(-500, 1500)):
        self.boids = boids
        self.x_limits = x_limits
        self.y_limits = y_limits
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=self.x_limits, ylim=self.y_limits)
        self.scatter = self.ax.scatter(self.boids[0], self.boids[1])

    def update_boids(self):
        xs, ys, xvs, yvs = self.boids
        move_to_middle_strength = 0.01
        alert_distance = 100
        formation_flying_distance = 10000
        formation_flying_strength = 0.125
        # Fly towards the middle
        for i in range(len(xs)):
            for j in range(len(xs)):
                xvs[i]=xvs[i]+(xs[j]-xs[i])*move_to_middle_strength/len(xs)
                yvs[i]=yvs[i]+(ys[j]-ys[i])*move_to_middle_strength/len(xs)
        # Fly away from nearby boids
                if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < alert_distance:
                    xvs[i]=xvs[i]+(xs[i]-xs[j])
                    yvs[i]=yvs[i]+(ys[i]-ys[j])
        # Try to match speed with nearby boids
        for i in range(len(xs)):
            for j in range(len(xs)):
                if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < formation_flying_distance:
                    xvs[i]=xvs[i]+(xvs[j]-xvs[i])*formation_flying_strength/len(xs)
                    yvs[i]=yvs[i]+(yvs[j]-yvs[i])*formation_flying_strength/len(xs)
        # Move according to velocities
        for i in range(len(xs)):
            xs[i]=xs[i]+xvs[i]
            ys[i]=ys[i]+yvs[i]
        self.boids = xs, ys, xvs, yvs

    def animate(self, frame):
        self.update_boids()
        self.scatter.set_offsets(zip(self.boids[0], self.boids[1]))


def new_flock(count, xlimits, ylimits, vxlimits, vylimits):
    boids_x = [random.uniform(*xlimits) for x in range(count)]
    boids_y = [random.uniform(*ylimits) for x in range(count)]
    boid_x_velocities = [random.uniform(*vxlimits) for x in range(count)]
    boid_y_velocities = [random.uniform(*vylimits) for x in range(count)]
    return boids_x, boids_y, boid_x_velocities, boid_y_velocities
