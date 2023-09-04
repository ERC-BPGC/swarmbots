import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
plt.xlim(0, 10)
plt.ylim(0, 10)


robot = plt.Circle((2, 5), 0.3, color='blue')
obstacle = plt.Circle((7, 0), 0.5, color='red')


ax.add_patch(robot)
ax.add_patch(obstacle)


robot_x = 2
robot_y = 5
robot_vx = 0.1
robot_vy = 0
obs_y = 0
obs_x = 1
obs_vy = 0
robot_goal = (9,5)

avoidance_distance = 1.2


def update(frame):
    global robot_x, robot_y, robot_vx, robot_vy, obs_x, obs_y, obs_vy


    distance = np.sqrt((robot_x - 7)**2 + (robot_y - 5)**2)
    vel = np.sqrt((robot_vx-0.2)**2 + (robot_vy-0.2)**2) # rel vel
    t2c = (distance - (0.8))/vel

    if t2c<10:
        # away_x = np.abs((robot_x - 7) / distance)
        # away_y = np.abs((robot_y - 5) / distance)

        # # robot_vx = 0.05 * away_x
        # # robot_vx -= 0.05*away_x
        # # 
        robot_vy += 0.05
        
        if (robot_vx -0.05*away_x) >0:
            robot_vx -= 0.05*away_x


        robot_x += robot_vx
        robot_y += robot_vy

    else:
        print(robot_x,robot_y)
        if robot_y !=5:
            if robot_y > 5:
                robot_vy -=0.1 
            else:
                robot_vy +=0.1 
        elif robot_y ==5:
            robot_vy =0
        if robot_x !=9:
            robot_vx +=0.01

        if np.abs((robot_x-9))<1 and np.abs((robot_y-5))<1:
            if np.abs((robot_x-9))<0.01 and np.abs((robot_y-5))==0:
                robot_vx = 0
                robot_vy = 0
            elif np.abs((robot_x-9))<0.2: 
                robot_vx = 0.01
                robot_vy = 0
            else:
                robot_vx = 0.05
                robot_vy = 0
        

        # robot_vx = 0.1
        # robot_vy = 0 
        robot_x += robot_vx
        robot_y += robot_vy
    
    obs_y += 0.3
    obs_x += 0.2

    robot.center = (robot_x, robot_y)
    obstacle.center = (obs_x,obs_y)
    return robot, obstacle


ani = FuncAnimation(fig, update, frames=np.arange(0, 50), interval=200, blit=True)

plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Robot Obstacle Avoidance')
plt.show()