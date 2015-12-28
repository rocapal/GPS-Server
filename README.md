# GPS-Server
GPS Server Component to get geolocation through GPS in the RaspBerryPi board


## Compile

Just you need to run cmake in order to build the interfaces python files

```sh
cmake .
```
## Interface

The ice file defines the interface that you can use yto ask the server about the gps location. The structure is the following:

```sh
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

```


## Run

```sh
$ python GpsServer.py
Service init ...
```

```sh
$ python GpsClient.py  
object #0 (::tools::GPSData)
{
    latitude = 45.3453979492
    longitude = -5.8490717411
    altitude = 697.099975586
    speed = 0.319000005722
    utc = 2015-12-28T15:39:35.000Z
}
``` 
