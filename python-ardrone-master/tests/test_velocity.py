import ps_drone
import time
drone = ps_drone.Drone

drone.startup()
test = 1
drone.takeoff()
#test speed = 1
if test == 1:
    drone.moveForward(0.2)
elif test == 2:
    drone.moveForward(0.4)
elif test == 3:
    drone.moveForward(0.6)
elif test == 4:
    drone.moveForward(0.8)
elif test == 5:
    drone.moveForward(1)
elif test == 6:
    for i in xrange(3):
        drone.moveForward(0.2)
        time.sleep(0.2)
elif test == 7:
    for i in xrange(3):
        drone.moveForward(0.4)
        time.sleep(0.2)
elif test == 8:
    for i in xrange(3):
        drone.moveForward(0.6)
        time.sleep(0.2)
elif test == 9:
    for i in xrange(3):
        drone.moveForward(0.8)
        time.sleep(0.2)
elif test == 10:
    for i in xrange(3):
        drone.moveForward(1)
        time.sleep(0.2)
drone.land()
