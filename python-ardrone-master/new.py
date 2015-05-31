import libardrone
import pygame
pygame.init()
W, H = 320, 240
screen = pygame.display.set_mode((W, H))

drone = libardrone.ARDrone()
drone.reset()
drone.takeoff()
running = True
while running:
        #print('hello')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('hello')
                    drone.land()
                if event.key == pygame.K_UP:
                    drone.move_up()
                    print('move_up')
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_DOWN:
                    drone.move_down()

drone.land()
drone.halt()