from math import degrees, atan2

def contents(data):
  html = \
  '<html>\
    <head>\
      <meta name="viewport" content="width=device-width, initial-scale=1">\
      <style>\
        form {\
          margin-top: 2rem;\
        }\
      </style>\
    </head>\
    <body>\
      <form method="GET">\
        <input type="submit" name="cmd" value="1"> Calibrate the Geomagnetic Sensor\
      </form>\
      <p>Offset of X : ' + str(data.offsetX) + '</p>\
      <p>Offset of Y : ' + str(data.offsetY) + '</p>\
      <form method="GET">\
        <input type="submit" name="cmd" value="2"> Set the direction\
      </form>\
      <form method="GET">\
        <input type="submit" name="cmd" value="3"> Check the directional differences\
      </form>\
      <p>Directional Difference : ' + str(degrees(data.directionalDifference())) + '</p>\
      <form method="GET">\
        <input type="submit" name="cmd" value="4"> Leave\
        <p>Direction : <input type="number" name="direction" value="' + str(degrees(atan2(data.targetDirectionX, data.targetDirectionY))) + '"></p>\
        <p>Driving time : <input type="number" name="drivingTime"></p>\
      </form>\
    </body>\
  </html>'
  return html