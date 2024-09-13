from setuptools import setup

NAME = "pyswarm"
DESCRIPTION = "Python Package for Multi-Agent Robot Algorithm Simulation"
REPOSITORY = "https://github.com/ERC-BPGC/swarmbots"
EMAIL = "arjunputhli2003@gmail.com"
AUTHOR = "Electronics and Robotics Club (ERC) BITS Goa"
REQUIRES_PYTHON = ">=3.12.5"
VERSION = "0.0.1"
KEYWORDS = ("path planning", "robotics", "motion planning", "navigation", "algorithms", "multi-agent", "swarm", "simulator")

setup(
    name=NAME,
    version=VERSION,    
    description=DESCRIPTION,
    url=REPOSITORY,
    author=AUTHOR,
    author_email=EMAIL,
    license='MIT',
    packages=['pyswarm'],
    install_requires=['matplotlib',
                      'shapely',
                      'numpy',
                      ],
)
