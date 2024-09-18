from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

class Environment():
    """
    Base class for an Environment

    An environment object should encapsulate all 
    objects represented in the environment space
    and should provide a step-specific status
    checking API
    """

    def __init__(self):
        self.robots = []
        self.obstacles = []
        self.step_size = 0
        self.fig, self.ax = plt.subplots()
        self.animation = None
    
    @abstractmethod
    def add_robot(self, robot):
        """
        Adds a robot to the environment's robot list
        """

        raise NotImplementedError

    @abstractmethod
    def add_obstacle(self, obstacle):
        """
        Adds an environment obstacle
        """

        raise NotImplementError

    @abstractmethod
    def step(self):
        """
        Takes an incremental step
        """

        raise NotImplementedError


