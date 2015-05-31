import ps_drone
import time
drone = ps_drone.Drone()

drone.reset()
drone.startup()
test = 14
drone.takeoff()
#test speed = 1
time.sleep(7)
if test == 1:
    #35 / 50
    drone.moveForward(0.2)
elif test == 2:
    #120
    drone.moveForward(0.4)
elif test == 3:
    #140
    drone.moveForward(0.6)
elif test == 4:
    #175
    drone.moveForward(0.8)
elif test == 5:
    #190
    drone.moveForward(1)
elif test == 6:
    #180
    for i in xrange(3):
        drone.moveForward(0.2)
        time.sleep(0.2)
elif test == 7:
    #360
    for i in xrange(3):
        drone.moveForward(0.4)
        time.sleep(0.2)
elif test == 8:
    #160
    for i in xrange(3):
        drone.moveLeft(0.2)
        time.sleep(0.2)
elif test == 9:
    #330
    for i in xrange(3):
        drone.moveLeft(0.4)
        time.sleep(0.2)
elif test == 10:
    #4.7 sec
    t = time.time()
    drone.turnAngle(90,0.2)
    print(time.time() - t)
    time.sleep(0.2)
elif test == 11:
    #2.9 sec /2.2 - 0.6/ 1.6 - 1
    t = time.time()
    drone.turnAngle(90,1)
    print(time.time() - t)
    time.sleep(0.2)

elif test == 12:
    #1 - 4/ 30 - 0.8
    t = time.time()
    drone.turnAngle(30, 1)
    print(time.time() - t)
    time.sleep(0.2)
elif test == 13:
    for i in xrange(12):
        if i % 2 == 0:
            t = time.time()
            drone.moveLeft(0.3)
            print(time.time() - t)
            time.sleep(1)
            drone.moveForward(0.2)
            time.sleep(0.2)

            drone.hover()
        else:
            drone.turnAngle(60, 1)
elif test == 14:
    # drone.moveBackward(0.4)
    # time.sleep(0.8)
    for i in range(6):
        # drone.move(0.1, 0.02, 0, 0)
        drone.move(0.08, 0.05, 0, -0.45)
        time.sleep(0.8)
        # drone.land()
        # break
        # drone.turnAngle(-60, 1)

elif test == 15:
    import pygame
    pygame.init()
    W, H = 320, 240
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    r = True
    while r:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    drone.land()
                if event.key == pygame.K_q:
                    r = False
            drone.setConfigAllID()                              # Go to multiconfiguration-mode
            drone.sdVideo()                                     # Choose lower resolution (try hdVideo())
            drone.frontCam()                                    # Choose front view
            CDC = drone.ConfigDataCount
            while CDC==drone.ConfigDataCount: time.sleep(0.001) # Wait until it is done (after resync)
            drone.startVideo()                                  # Start video-function
            drone.showVideo()                                   # Display the video
        # except:
        #     pass

        pygame.display.flip()
        clock.tick(50)
        # pygame.display.set_caption("FPS: %.2f" % clock.get_fps())

time.sleep(1)
drone.hover()
time.sleep(3)
drone.land()
