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
from sys import stdout 
import Ice
import sys
sys.path.insert(0, './interfaces/python')
import tools

ic = None

ic = Ice.initialize(sys.argv)
base = ic.stringToProxy("GPS:default -h 0.0.0.0 -p 9000")
gps_server = tools.GPSPrx.checkedCast(base)
if not gps_server:
    raise RuntimeError("Invalid proxy")

data = gps_server.getLocation()
print data

