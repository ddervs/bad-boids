from setuptools import setup, find_packages

setup(
    name="Boids",
    version="0.1.0",
    packages=find_packages(exclude=['*tests']),
    scripts=['scripts/boids'],
    install_requires=['numpy', 'matplotlib', 'mock', 'pyyaml']
)