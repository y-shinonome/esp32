from math import degrees, atan2

def contents(gy271, motor):
  html = \
  '<html>\
    <head>\
      <meta name="viewport" content="width=device-width, initial-scale=1">\
      <style>\
        html {\
          font-family: Roboto;\
        }\
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
          margin-bottom: 1.5rem;\
        }\
        input {\
          font-size: 1em;\
        }\
        .conf {\
          width: 10rem;\
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
        <h3>Drive the drone<span id="timer"></span></h3>\
        <form method="GET">\
          <input type="submit" name="cmd" value="drive">\
          <p>Direction : <input type="number" class="conf" name="direction" value="' + str(degrees(atan2(gy271.targetDirectionX, gy271.targetDirectionY))) + '"></p>\
          <p>Driving time : <input type="number" id="driving_time" class="conf" name="driving_time" value="' + str(motor.drivingTime) + '"></p>\
          <p>Small coefficient : <input type="number" class="conf" name="small_coefficient" value="' + str(motor.smallCoefficient) + '"></p>\
          <p>Large coefficient : <input type="number" class="conf" name="large_coefficient" value="' + str(motor.largeCoefficient) + '"></p>\
          <p>Max duty(ns) : <input type="number" class="conf" name="max_duty_ns" value="' + str(motor.maxDuty_ns) + '"></p>\
        </form>\
      </div>\
      <div>\
        <h3>Stop the drone</h3>\
        <form method="GET">\
          <input type="submit" name="cmd" value="stop">\
        </form>\
      </div>\
      <div>\
        <h3>Reset the device</h3>\
        <form method="GET">\
          <input type="submit" name="cmd" value="reset">\
        </form>\
      </div>\
      <script>\
        window.onload = () => {\
          let count = document.getElementById("driving_time").value;\
          const countdown = setInterval(() => {\
            if (count == 0) {\
              clearInterval(countdown);\
              timer.innerHTML="";\
            } else {\
              count --;\
              timer.innerHTML = " : " + String(count);\
            }\
          } ,1000);\
        }\
      </script>\
    </body>\
  </html>'
  return html