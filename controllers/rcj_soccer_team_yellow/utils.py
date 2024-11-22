import math


def definitions(robot):
    robot.heading = 0
    robot.xr = 0
    robot.yr = 0
    robot.xb = 0
    robot.yb = 0
    robot.is_ball = False

def moveTo(robot, x, y, s=False):
    a = math.degrees(math.atan2((robot.xr-x), -(robot.yr-y)))
    e = robot.heading - a
    if e >  180: e -= 360
    if e < -180: e += 360

    # if -0.01 < robot.xr -x < 0.01 and -0.01 < robot.yr - y < 0.01:
    #     right_speed = 0
    #     left_speed = 0
    # else:
    if e > -90 and e < 90:
        right_speed = 10 + e*0.3
        left_speed =  10 - e*0.3
    else:
        if e > 0: e -= 180
        else:     e += 180
        right_speed = -10 + e*0.3
        left_speed =  -10 - e*0.3
    
    if right_speed >  10: right_speed =  10
    if right_speed < -10: right_speed = -10
    if left_speed >  10: left_speed =  10
    if left_speed < -10: left_speed = -10
    if abs(robot.xr - x) < 0.01 and abs(robot.yr - y) < 0.01 and s:
        stop(robot)
    else:
        robot.right_motor.setVelocity(right_speed)
        robot.left_motor.setVelocity(left_speed)
def stop(robot):
    robot.right_motor.setVelocity(0)
    robot.left_motor.setVelocity(0)

def readData(robot):
    ########################################### محاسبه مختصات توپ
    gps = robot.get_gps_coordinates()
    robot.heading = math.degrees(robot.get_compass_heading())
    robot.xr = gps[0]
    robot.yr = gps[1]
    if robot.team == 'B':
        robot.xr *= -1
        robot.yr *= -1
    if robot.is_new_ball_data():
        ball_data = robot.get_new_ball_data()
        ball_angle = math.degrees(math.atan2(ball_data['direction'][1], ball_data['direction'][0]))
        ball_distance = abs(0.01666666/(abs(ball_data['direction'][2])/math.sqrt(1 - ball_data['direction'][2]**2)))
        robot.xb = -math.sin(math.radians(ball_angle + robot.heading)) * ball_distance + robot.xr
        robot.yb =  math.cos(math.radians(ball_angle + robot.heading)) * ball_distance + robot.yr
        robot.is_ball = True
    else:
        robot.is_ball = False
    ########################################### ارسال اطلاعات به بقیه ربات ها
    robot.send_data_to_team({
        'is_ball': robot.is_ball,
        'xb': robot.xb,
        'yb': robot.yb,
        'xr': robot.xr,
        'yr': robot.yr,
        'id': robot.player_id
    })
    ########################################### دریافت اطلاعات از ربات
    while robot.is_new_team_data():
        team_data = robot.get_new_team_data()['robot_id']
        if not robot.is_ball and team_data['is_ball']:
            robot.is_ball = True
            robot.xb = team_data['xb']
            robot.yb = team_data['yb']




