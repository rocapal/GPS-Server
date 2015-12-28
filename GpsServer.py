#!/usr/bin/env python

#  Copyright (C) 2015
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see http://www.gnu.org/licenses/.
#
#  Authors : Roberto Calvo <rocapal at gmail dot com>

import os
from gps import *
from time import *
import time
import threading
from sys import stdout 
import RPi.GPIO as GPIO
import signal

import Ice
import sys
sys.path.insert(0, './interfaces/python')
import tools


#os.system('sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock')


class GpsPoller(threading.Thread):

    def __init__(self):
	threading.Thread.__init__(self)
 	self.gpsd = None
 	self.gpsd = gps(mode=WATCH_ENABLE) 
 	self.current_value = None
 	self.running = True 
        
    def run(self):
	while self.running:
	    self.gpsd.next()

    def getGPS(self):
        return self.gpsd

class GPSI(tools.GPS):


    def __init__(self, gpsp):

        self.gpsp = gpsp
        self.gpsp.start()

        print "Service init ... "

    def getLocation(self, current=None):
        if (self.gpsp.getGPS().fix.mode == MODE_NO_FIX):
            return None
        else:
            data = tools.GPSData()
            data.altitude = self.gpsp.getGPS().fix.altitude
            data.latitude = self.gpsp.getGPS().fix.latitude
            data.longitude = self.gpsp.getGPS().fix.longitude
            data.utc = self.gpsp.getGPS().utc
            data.speed = self.gpsp.getGPS().fix.speed

            return data





if __name__ == '__main__':

    gpsp = GpsPoller()

    ic = None
    try:
        ic = Ice.initialize(sys.argv)
        adapter = ic.createObjectAdapterWithEndpoints("GPSAdapter", "default -p 9000")
        object = GPSI(gpsp)
        adapter.add(object, ic.stringToIdentity("GPS"))
        adapter.activate()
        ic.waitForShutdown()

    except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
	print "\nKilling Thread..."

        if gpsp.is_alive():
	    gpsp.running = False
	    gpsp.join()


        if (ic):
            ic.destroy()


