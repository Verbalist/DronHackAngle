__author__ = 'dima'

import libardrone
import pygame

f = open('log.txt','a\n')

pygame.init()
W, H = 320, 240
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

drone = libardrone.ARDrone()
drone.reset()
drone.takeoff()

def move_in_m(drone, count, clock):
    i = 0
    while (i < count):
        drone.move_forward()
        clock.tick(50)
        i+=1


running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                f.write('quit\n')
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    drone.land()
                    f.write('land\n')
                if event.key == pygame.K_UP:
                    drone.move_up()
                    f.write('move_up\n')
                if event.key == pygame.K_ESCAPE:
                    running = False
                    f.write('Exit\n')
                if event.key == pygame.K_DOWN:
                    drone.move_down()
                    f.write('move_down\n')
                if event.key == pygame.K_1:
                    move_in_m(drone, 10, clock)
                    f.write('10\n')
                if event.key == pygame.K_2:
                    move_in_m(drone, 10, clock)
                    f.write('20\n')
                if event.key == pygame.K_RETURN:
                    drone.takeoff()
                    f.write('takeoff\n')
                if event.key == pygame.K_LCTRL:
                    drone.reset()
                    f.write('reset\n')
                if event.key == pygame.K_w:
                    drone.move_forward()
                    f.write('forward\n')
                if event.key == pygame.K_s:
                    drone.move_backward()
                    f.write('back\n')
                if event.key == pygame.K_a:
                    drone.move_left()
                    f.write('left\n')
                if event.key == pygame.K_d:
                    drone.move_right()
                    f.write('right\n')
                if event.key == pygame.K_w:
                    drone.move_forward()
                if event.key == pygame.K_LEFT:
                    drone.turn_left()
                    f.write('left\n')
                if event.key == pygame.K_RIGHT:
                    drone.turn_right()
                    f.write('right\n')
                if event.key == pygame.K_LCTRL:
                    bat = drone.navdata.get(0, dict()).get('battery', 0)
                    f.write(bat)

#<<<<<<< Updated upstream:python-ardrone-master/main.py
        # try:
        #     clock.tick(50)
        #
        # except:
        #     f.write('err\n')
#=======
                if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_1):
                    drone.speed = 0.1
                if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_2):
                    drone.speed = 0.2
                if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_3):
                    drone.speed = 0.3
                if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_4):
                    drone.speed = 0.4
                if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_5):
                    drone.speed = 0.5
                if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_6):
                    drone.speed = 0.6
                if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_7):
                    drone.speed = 0.7
                if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_8):
                    drone.speed = 0.8
                if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_9):
                    drone.speed = 0.9
                if (event.key == pygame.KMOD_LCTRL and event.key == pygame.K_0):
                    drone.speed = 1.0

        try:
            clock.tick(50)

        except:
            f.write('err\n')
#>>>>>>> Stashed changes:python-ardrone-master/main.py

#end demonstration
drone.land()
drone.halt()