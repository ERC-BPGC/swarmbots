from envs.world import World

class Simulate():
    def __init__(self):
        world = World(13,7)
        world.initiate_world(100)

        print(len(world.robots))
        print(world.robots[0].pos_x,world.robots[0].pos_y)