class Robot():
    def __init__(self, pos_x,pos_y,vel_x,vel_y,radius,neighbors : list, rob_plt):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.radius = radius
        self.neighbors = neighbors
        self.rob_plt = rob_plt #matplotlib element

        