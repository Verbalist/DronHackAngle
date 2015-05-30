__author__ = 'dima'

import libardrone
import pygame

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


running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print('quit')
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    drone.land()
                    print('land')
                if event.key == pygame.K_UP:
                    drone.move_up()
                    print('move_up')
                if event.key == pygame.K_ESCAPE:
                    running = False
                    print('Exit')
                if event.key == pygame.K_DOWN:
                    drone.move_down()
                    print('move_down')
                if event.key == pygame.K_1:
                    move_in_m(drone, 10, clock)
                    print('10')
                if event.key == pygame.K_2:
                    move_in_m(drone, 10, clock)
                    print('20')
                if event.key == pygame.K_RETURN:
                    drone.takeoff()
                    print('takeoff')
                if event.key == pygame.K_LCTRL:
                    drone.reset()
                    print('reset')
                if event.key == pygame.K_w:
                    drone.move_forward()

                if event.key == pygame.K_LCTRL:
                    bat = drone.navdata.get(0, dict()).get('battery', 0)
                    print(bat)

        try:
            clock.tick(50)

        except:
            print('err')

#end demonstration
drone.land()
drone.halt()