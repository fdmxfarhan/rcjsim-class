import math


def moveTo(robot, x, y):
    gps = robot.get_gps_coordinates()
    heading = math.degrees(robot.get_compass_heading())

    xr = gps[0]
    yr = gps[1]
    
    a = math.degrees(math.atan2((xr-x), -(yr-y)))
    e = heading - a
    if e >  180: e -= 360
    if e < -180: e += 360

    # if -0.01 < xr -x < 0.01 and -0.01 < yr - y < 0.01:
    #     right_speed = 0
    #     left_speed = 0
    # else:
    right_speed = 10 + e*0.3
    left_speed =  10 - e*0.3
    
    if right_speed >  10: right_speed =  10
    if right_speed < -10: right_speed = -10
    if left_speed >  10: left_speed =  10
    if left_speed < -10: left_speed = -10
    robot.right_motor.setVelocity(right_speed)
    robot.left_motor.setVelocity(left_speed)

def stop(robot):
    robot.right_motor.setVelocity(0)
    robot.left_motor.setVelocity(0)