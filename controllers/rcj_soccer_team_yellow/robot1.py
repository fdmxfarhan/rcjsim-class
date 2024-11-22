from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP
import utils
import keyboard

class MyRobot1(RCJSoccerRobot):
    def run(self):
        utils.definitions(self)
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                utils.readData(self)
                if keyboard.is_pressed('w'):
                    self.left_motor.setVelocity(10)
                    self.right_motor.setVelocity(10)
                if keyboard.is_pressed('s'):
                    self.left_motor.setVelocity(-10)
                    self.right_motor.setVelocity(-10)
                
                # if self.is_ball:
                #     utils.moveTo(self, self.xb, -0.55)
                # else:
                #     utils.moveTo(self, 0, -0.5, s=True)