from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import math
import utils

class MyRobot2(RCJSoccerRobot):
    def run(self):
        state = 1
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                gps = self.get_gps_coordinates()
                heading = math.degrees(self.get_compass_heading())
                xr = gps[0]
                yr = gps[1]
                if self.is_new_ball_data():
                    ball_data = self.get_new_ball_data()
                    ball_angle = math.degrees(math.atan2(ball_data['direction'][1], ball_data['direction'][0]))
                    ball_distance = abs(0.01666666/(abs(ball_data['direction'][2])/math.sqrt(1 - ball_data['direction'][2]**2)))
                    xb = -math.sin(math.radians(ball_angle + heading)) * ball_distance + xr
                    yb =  math.cos(math.radians(ball_angle + heading)) * ball_distance + yr
                    if state == 1:
                        utils.moveTo(self, xb, yb - 0.15)
                        if abs(xb - xr) < 0.01 and abs((yb-0.15) - yr) < 0.01:
                            state = 2
                    elif state == 2:
                        utils.moveTo(self, xb, yb)
                        if abs(xb - xr) > 0.2 or abs(yb - yr) > 0.2:
                            state = 1
                else:
                    utils.stop(self)