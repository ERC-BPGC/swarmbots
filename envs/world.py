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
        plt.xlim(0, 100)
        plt.ylim(0, 100)
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
            x0 = random.uniform(0,93)
            y0 = random.uniform(7,100)
            x1 = x0 + side_length
            y1 = y0 - side_length
            if len(self.obstacles) !=0:
                for i in self.obstacles:
                    if((x1 in np.arange(i.x0,i.x1) or x0 in np.arange(i.x0,i.x1)) and ( y1 in np.arange(i.y1,i.y0) or y0 in np.arange(i.y1,i.y0))):
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
            x0 = random.uniform(1.5,98.5) 
            y0 = random.uniform(1.5,98.5)
            print("here")
            x1 = x0 - r 
            y1 = y0 - r
            x2 = x0 + r
            y2 = y0 + r
            if len(self.obstacles) !=0:
                for i in self.obstacles:
                    if((x1 in np.arange(i.x0,i.x1) or x2 in np.arange(i.x0,i.x1)) and ( y1 in np.arange(i.y1,i.y0) or y2 in np.arange(i.y1,i.y0))):
                        bool = False #above condition was to check if this new robot is not overlapping with any existing obstacle
                        break
                    else:  
                        bool = True
            else:
                bool = True
    
            if bool == True:
                if len(self.robots)!=0:
                    for i in self.robots:
                        if((x1 in np.arange(i.pos_x - i.radius,i.pos_x +i.radius) or x2 in np.arange(i.pos_x - i.radius,i.pos_x +i.radius)) and ( y1 in np.arange(i.pos_y - i.radius,i.pos_y +i.radius) or y2 in np.arange(i.pos_y - i.radius,i.pos_y +i.radius))):
                            bool = False  #above condition was to check if this new robot is not overlapping with any existing robot
                            break
                        else:  
                            bool = True

                else:
                    bool = True
        rob_plt = plt.Circle((x0, y0), 1.5, color='blue')
        robot = Robot(x0,y0,0,0,1.5,[],rob_plt)
        
        
        return robot