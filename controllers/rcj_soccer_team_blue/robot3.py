from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import math
import utils

class MyRobot3(RCJSoccerRobot):
    def run(self):
        state = 1
        utils.definitions(self)
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                utils.readData(self)
                if self.is_ball:
                    if state == 1:
                        utils.moveTo(self, self.xb, self.yb - 0.15)
                        if abs(self.xb - self.xr) < 0.01 and abs((self.yb-0.15) - self.yr) < 0.05:
                            state = 2
                    elif state == 2:
                        utils.moveTo(self, self.xb, self.yb)
                        if abs(self.xb - self.xr) > 0.2 or abs(self.yb - self.yr) > 0.2:
                            state = 1
                else:
                    utils.moveTo(self, 0.3, -0.2, s=True)