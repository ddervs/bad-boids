from setuptools import setup, find_packages

setup(
    name="Boids",
    version="1.0.0",
    packages=find_packages(exclude=['*tests']),
    scripts=['scripts/boids'],
    install_requires=['numpy', 'matplotlib', 'mock', 'pyyaml'],
    include_package_data=True,
    package_data={'boids': ['*.yaml']}
)
