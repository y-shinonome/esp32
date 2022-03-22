from math import degrees, atan2

def contents(gy271, motor):
  html = \
  '<html>\
    <head>\
      <meta name="viewport" content="width=device-width, initial-scale=1">\
      <style>\
        h3 {\
          margin: 0.5rem;\
        }\
        p {\
          margin: 0.5rem;\
          margin-left: 1.5rem;\
        }\
        form {\
          margin: 0.5rem;\
          margin-left: 1.5rem;\
        }\
        form > p {\
          margin-left: 0rem;\
        }\
        div {\
          margin-bottom: 2rem;\
        }\
      </style>\
    </head>\
    <body>\
      <div>\
        <h3>Calibrate the Geomagnetic Sensor</h3>\
        <form method="GET">\
          <input type="submit" name="cmd" value="calibrate">\
        </form>\
        <p>Offset of X : ' + str(gy271.offsetX) + '</p>\
        <p>Offset of Y : ' + str(gy271.offsetY) + '</p>\
      </div>\
      <div>\
        <h3>Set the direction</h3>\
        <form method="GET">\
          <input type="submit" name="cmd" value="set">\
        </form>\
        <p>Direction : ' + str(degrees(atan2(gy271.targetDirectionX, gy271.targetDirectionY))) + '</p>\
      </div>\
      <div>\
        <h3>Check the directional differences</h3>\
        <form method="GET">\
          <input type="submit" name="cmd" value="check">\
        </form>\
        <p>Directional Difference : ' + str(degrees(gy271.directionalDifference())) + '</p>\
      </div>\
      <div>\
        <h3>Drive the drone</h3>\
        <form method="GET">\
          <input type="submit" name="cmd" value="drive">\
          <p>Direction : <input type="number" name="direction" value="' + str(degrees(atan2(gy271.targetDirectionX, gy271.targetDirectionY))) + '"></p>\
          <p>Driving time : <input type="number" name="driving_time" value="' + str(motor.drivingTime) + '"></p>\
          <p>Small coefficient : <input type="number" name="small_coefficient" value="' + str(motor.smallCoefficient) + '"></p>\
          <p>Large coefficient : <input type="number" name="large_coefficient" value="' + str(motor.largeCoefficient) + '"></p>\
          <p>Max duty(ns) : <input type="number" name="max_duty_ns" value="' + str(motor.maxDuty_ns) + '"></p>\
        </form>\
      </div>\
    </body>\
  </html>'
  return html