from setuptools import setup, find_packages

setup(
    name="Boids",
    version="1.0.0",
    author='Danial Dervovic',
    author_email='danial.dervovic.11@ucl.ac.uk',
    url='https://github.com/ddervs/bad-boids',
    packages=find_packages(exclude=['*tests']),
    scripts=['scripts/boids'],
    install_requires=['numpy', 'matplotlib', 'mock', 'pyyaml'],
    include_package_data=True,
    package_data={'boids': ['*.yaml']}
)
