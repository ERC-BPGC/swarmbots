import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random 

fig, ax = plt.subplots()
plt.xlim(0, 30)
plt.ylim(0, 30)


robot = plt.Circle((2, 5), 0.3, color='blue')
obstacle = plt.Circle((7, 0), 0.5, color='red')


ax.add_patch(robot)
ax.add_patch(obstacle)


robot_x,robot_y = tuple(map(int,input("robot coords").split()))
robot_vx, robot_vy = (0.01,0.01)
obs_x, obs_y = tuple(map(int,input("obs coords").split()))
obs_vx, obs_vy = (random.uniform(-0.02,0.02),random.uniform(-0.02,0.02))
robot_goal_x, robot_goal_y = tuple(map(int,input("robot goal coords").split()))



def update(frame):
    global robot_x, robot_y, robot_vx, robot_vy, obs_x, obs_y, obs_vy, obs_vx


    distance = np.sqrt((robot_x - obs_x)**2 + (robot_y - obs_y)**2)
    vel = np.sqrt((robot_vx-obs_vx)**2 + (robot_vy-obs_vy)**2) # rel vel
    t2c = (distance - (0.8))/vel

    if t2c<8:
        away_x = (robot_x - obs_x)
        away_y = (robot_y - obs_y)
        # if t2c<1:
        
        if away_y < 0:
            robot_vy -= 0.02
        if away_y >0:
            robot_vy +=0.02
        
        if away_y ==0:
            robot_vy = -0.02

        if away_x >0.8:
            robot_vx += 0.01
        elif away_x <-0.8:
            robot_vx -= 0.01
        else:
            robot_vx += 0.01

        robot_x += robot_vx
        robot_y += robot_vy


    else:


        print(robot_x,robot_y)

        if np.abs((robot_x-robot_goal_x))>1:
            if robot_x > robot_goal_x:
                robot_vx -=0.02 
            else:
                robot_vx +=0.02
        elif robot_x ==robot_goal_x :
            robot_vx =0

        else:
            if robot_x >robot_goal_x:
                if (robot_x-robot_goal_x)<0.01:
                    robot_vx =0
                elif (robot_x-robot_goal_x)<0.2:
                    robot_vx = -0.01
                else:
                    robot_vx = -0.05
            else:
                if np.abs((robot_x-robot_goal_x))<0.01:
                    robot_vx =0
                elif np.abs((robot_x-robot_goal_x))<0.2:
                    robot_vx = 0.01
                else:
                    robot_vx = 0.05


        if np.abs((robot_y-robot_goal_y))>1:
            if robot_y > robot_goal_y:
                robot_vy -=0.02
            else:
                robot_vy +=0.02
        elif robot_y ==robot_goal_y :
            robot_vy =0
        else:
            if robot_y >robot_goal_y:
                if (robot_y-robot_goal_y)<0.01:
                    robot_vy =0
                elif (robot_y-robot_goal_y)<0.2:
                    robot_vy = -0.01
                else:
                    robot_vy = -0.02
            else:
                if np.abs((robot_y-robot_goal_y))<0.01:
                    robot_vy =0
                elif np.abs((robot_y-robot_goal_y))<0.2:
                    robot_vy = 0.01
                else:
                    robot_vy = 0.02

        # robot_vx = 0.1
        # robot_vy = 0 
        if np.abs(robot_vy)> 0.1:
            if robot_vy >0 :
                robot_vy = 0.1
            else:
                robot_vy = -0.1
        if np.abs(robot_vx)> 0.1:
            if robot_vx >0:
                robot_vx = 0.1
            else:
                robot_vx = -0.1
        robot_x += robot_vx
        robot_y += robot_vy
    
    obs_vy -= 0.01
    obs_vx -=0.01

    if np.abs(obs_vy) > 0.07:
        if(obs_vy)>0:
            obs_vy = 0.07
        else:
            obs_vy = -0.07
    if np.abs(obs_vx) > 0.07:
        if(obs_vx)>0:
            obs_vx = 0.07
        else:
            obs_vx = -0.07
    obs_y += obs_vy
    obs_x += obs_vx

    robot.center = (robot_x, robot_y)
    obstacle.center = (obs_x,obs_y)
    return robot, obstacle


ani = FuncAnimation(fig, update, frames=np.arange(0, 50), interval=200, blit=True)

plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Robot Obstacle Avoidance')
plt.show()