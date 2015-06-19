__author__ = 'Oliver'

import time
import random

#design climate control device

class climate_control(object):

    def __init__(self):
        self.initialize = 1
        self.state = True
        self.heat_on = 0
        self.a_c_on = 0
        self.display_text()

    def display_text(self):
        if self.initialize:
            print("CC Master Starting Up...")
            self.current = self.current_temp()
            print("Current temperature is: {}").format(self.current)
            self.ideal = self.set_base_temp()
            if (self.current - self.ideal) > 0:
                self.a_c()
            elif (self.current - self.ideal) < 0:
                self.heat()
            else:
                self.ideal_temp()

    def temp_change(self):
        while self.current != self.ideal:
            time.sleep(5)
            print("Temp is now: ")
            if self.heat_on:
                self.current += 1
                print self.current, self.heat()
            elif self.a_c_on:
                self.current -= 1
                print self.current, self.a_c()
        self.turn_off()

    def heat(self):
        if self.initialize:
            print("Starting to warm up...")
            self.initialize = 0
            self.heat_on = 1
            self.temp_change()
        else:
            return("Up +1...")

    def a_c(self):
        if self.initialize:
            print("Starting to cool off...")
            self.initialize = 0
            self.a_c_on = 1
            self.temp_change()
        else:
            return("Down -1...")


    def ideal_temp(self):
        print("Ideal temperature reached...")
        self.heat_on = 0
        self.a_c_on = 0
        if self.is_running():
            self.turn_off()

    def is_running(self):
        # returns True if running and False otherwise
        return self.state

    def current_temp(self):
        if self.initialize:
            self.current = random.randrange(45, 95)
            return self.current
        return self.current

    def set_base_temp(self):
        return int(raw_input("What would you like to set the temperature to? "))

    def turn_off(self):
        # turns off controller
        self.state = False
        print("Turning off Controller...")

cc = climate_control()