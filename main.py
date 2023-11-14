#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks import ev3brick as brick


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
    

    def shootCard(self):
        # run at 800 speed for 350 ms
        self.shootMotor.run_time(800, 350)
        # run at -1000 speed for 500 ms
        self.shootMotor.run_time(-1000, 500)
    
    def deal(self, players, amt, angle):
        self.turnMotor.run_target(turnRate, 0) # move to start position
        if players <= 1:
            brick.display.text("Canceled: Not enough players")
            return
        if amt <= 0:
            brick.display.text("Canceled: Invalid amount")
            return
        if angle <= 0 or angle > 180:
            brick.display.text("Canceled: Invalid angle")
            return
        self.turnMotor.run_angle(turnRate, -angle/2*turnRatio) # move to start position
        playerSpace = angle/(players-1) # angle between each player
        for i in range(amt): # deal amt cards
            for j in range(players-1): # deal to each player
                self.shootCard() # shoot card
                self.turnMotor.run_angle(turnRate, playerSpace*turnRatio) # move to next player
            self.shootCard()
            self.turnMotor.run_angle(turnRate, -angle*turnRatio) # move back to start position
        self.turnMotor.run_angle(turnRate, angle/2*turnRatio) # return to original position

robot = LEGORobotCardDealer(EV3Brick, Motor(port=Port.B), Motor(port=Port.C))

robot.deal(4, 2, 150)