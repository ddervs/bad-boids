Boids
=============

Implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406), used as an exercise on refactoring for the [UCL RSD Software Engineering course](http://development.rc.ucl.ac.uk/training/engineering/). Forked from [bad-boids](https://github.com/jamespjh/bad-boids).

Usage
=============

```
usage: boids [-h] [--config CONFIG] [--example_config]

Runs the boids simulation.

optional arguments:
  -h, --help        show this help message and exit
  --config CONFIG   YAML file with simulation options. See README.md or use
                    --example-config option for specification.
  --example_config  Saves default config file to current working directory.

```
Any variables not defined will be replaced by the default values below. 

Sample Config File
=============
```
move_to_middle_strength: 0.01
alert_distance: 100
formation_flying_distance: 10000
formation_flying_strength: 0.125
number_of_boids: 50
# Simulation initial conditions
x_initial: [-450, 50.0]
y_initial: [300.0, 600.0]
vx_initial: [0, 10.0]
vy_initial: [0, 10.0]
# Plot limits - need to be python tuples
x_plot_limits: [-500, 1500]
y_plot_limits: [-500, 1500]
# Animation parameters
frames: 50
interval: 50
```