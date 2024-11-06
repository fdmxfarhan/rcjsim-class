from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP

class MyRobot2(RCJSoccerRobot):
    def run(self):
        self.right_motor.setVelocity(0)
        self.left_motor.setVelocity(0)