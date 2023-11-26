import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random 
from utils.obstacle import Obstacle
from utils.robot import Robot
import numpy as np
class World():
    def __init__(self, num_robots, num_obstacles):
        self.num_robots = num_robots
        self.num_obstacles = num_obstacles
        self.robots = []
        self.obstacles = []
        fig, ax = plt.subplots()
        self.plt_lim =100
        plt.xlim(0, self.plt_lim)
        plt.ylim(0, self.plt_lim)
        for i in range(num_obstacles):
            obstacle = self.load_obstacle()
            ax.add_patch(obstacle.obs_plt)
            self.obstacles.append(obstacle)
        for _ in range(num_robots):
            robot = self.load_robot()
            ax.add_patch(robot.rob_plt)
            self.robots.append(robot)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('APF')
        plt.show()
    def load_obstacle(self):
        bool = False 
        side_length = 7
        while bool is False:
            x0 = random.uniform(0,self.plt_lim - side_length)
            y0 = random.uniform(side_length,self.plt_lim)
            x1 = x0 + side_length
            y1 = y0 - side_length
            if len(self.obstacles) !=0:
                for i in self.obstacles:
                    if (((x1>i.x0 and x1<i.x1) or (x0>i.x0 and x0<i.x1)) and ((y0 > i.y1 and y0 < i.y0) or (y1 >i.y1 and y1<i.y0))):
    
                        bool = False #above condition was to check if this new obstacle is not overlapping with any existing obstacle
                        break
                    else:  
                        bool = True
            else:
                bool = True
        obs_plt = plt.Rectangle((x0,y1), side_length, side_length, fc='red')
        obstacle = Obstacle(x0,y0,x1,y1,obs_plt)
        
        return obstacle

    def load_robot(self):
        bool = False 
        r = 1.5
        while bool is False:
            x0 = random.uniform(r,self.plt_lim-r) 
            y0 = random.uniform(r,self.plt_lim-r)
            print("here")
            x1 = x0 - r 
            y1 = y0 - r
            x2 = x0 + r
            y2 = y0 + r
            if len(self.obstacles) !=0:
                for i in self.obstacles:
                    if (((x1>i.x0 and x1<i.x1) or (x0>i.x0 and x0<i.x1)) and ((y0 > i.y1 and y0 < i.y0) or (y1 >i.y1 and y1<i.y0))):
                        bool = False #above condition was to check if this new robot is not overlapping with any existing obstacle
                        break
                    else:  
                        bool = True
            else:
                bool = True
    
            if bool == True:
                if len(self.robots)!=0:
                    for i in self.robots:
                        x1_b = i.pos_x - i.radius
                        y1_b = i.pos_y - i.radius
                        x2_b = i.pos_x + i.radius
                        y2_b = i.pos_y + i.radius
                        if (((x1>x1_b and x1<x2_b) or (x2 > x1_b and x2  <x2_b)) and ((y1 > y1_b and y1<y2_b) or (y2 >y1_b and y2<y2_b))):
                            bool = False  #above condition was to check if this new robot is not overlapping with any existing robot
                            break
                        else:  
                            bool = True

                else:
                    bool = True
        rob_plt = plt.Circle((x0, y0),r, color='blue')
        robot = Robot(x0,y0,0,0,r,[],rob_plt)
        
        
        return robot