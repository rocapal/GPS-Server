
/*
 *  Copyright (C) 
 *
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see http://www.gnu.org/licenses/.
 *
 *  Authors : Roberto Calvo <rocapal [at] gmail [dot] com>
 *
 */


#ifndef GPS_ICE
#define GPS_ICE


module tools {

       class GPSData
       {
           float latitude;
           float longitude;
           float altitude;
           float speed;
           string utc;
       };

       interface GPS
       {
          idempotent GPSData getLocation();
       };

};


#endif //GPS_ICE

