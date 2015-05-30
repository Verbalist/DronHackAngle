__author__ = 'dima'

import libardrone

class Drone(libardrone.ARDrone):

    def __init__(self, clock):
        super(Drone, self).__init__()
        self.clock = clock
        self.x = 0
        self.y = 0
        self.z = 0
        self.direct = 0

    def move_n_times(self, n, types):
        if types == 'forward':
            self.move_forward()
        elif types == 'backward':
            self.move_backward()

    def takeoff(self):
        """Make the drone takeoff."""
        self.at(libardrone.at_ftrim)
        self.at(libardrone.at_config, "control:altitude_max", "20000")
        self.at(libardrone.at_ref, True)
        self.z = 80

    def land(self):
        """Make the drone land."""
        self.at(libardrone.at_ref, False)
        self.z = 0

    def move_right(self, n):
        """Make the drone move right."""
        for i in n:
            self.at(libardrone.at_pcmd, True, self.speed, 0, 0, 0)
            self.clock.tick(50)

    def turn_left(self, n):
        """Make the drone rotate left."""
        for i in n:
            self.at(libardrone.at_pcmd, True, 0, 0, 0, -self.speed)
            self.clock.tick(50)

    def set_altitude(self, altitude):
        pass
        # self.move()

    def circle(self, R = 100):
        #сделать круг радиусом R
        pass

    def go_to_XYZ(self):
        pass

    def spiral(self, R=100, alt=100):
        pass


