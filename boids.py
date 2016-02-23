"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

boids_x = [random.uniform(-450, 50.0) for x in range(50)]
boids_y = [random.uniform(300.0, 600.0) for x in range(50)]
boid_x_velocities = [random.uniform(0, 10.0) for x in range(50)]
boid_y_velocities = [random.uniform(-20.0, 20.0) for x in range(50)]
boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)


def update_boids(boids):
    xs, ys, xvs, yvs = boids
    move_to_middle_strength = 0.01
    alert_distance = 100
    formation_flying_distance = 10000
    formation_flying_strength = 0.125
    # Fly towards the middle
    for i in range(len(xs)):
        for j in range(len(xs)):
            xvs[i] += (xs[j] - xs[i]) * move_to_middle_strength / len(xs)
            yvs[i] += (ys[j] - ys[i]) * move_to_middle_strength / len(xs)
    # Fly away from nearby boids
            if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < alert_distance:
                xvs[i] += (xs[i] - xs[j])
                yvs[i] += (ys[i] - ys[j])
    # Try to match speed with nearby boids
            if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < formation_flying_distance:
                xvs[i] += (xvs[j] - xvs[i]) * formation_flying_strength / len(xs)
                yvs[i] += (yvs[j] - yvs[i]) * formation_flying_strength / len(xs)
    # Move according to velocities
        xs[i] += xvs[i]
        ys[i] += yvs[i]


figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(boids[0], boids[1])


def animate(frame):
    update_boids(boids)
    scatter.set_offsets(zip(boids[0], boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
