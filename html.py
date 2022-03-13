def contents(data):
  html = \
  '<html>\
    <head>\
      <meta name="viewport" content="width=device-width, initial-scale=1">\
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
        <p>Direction : <input type="number" name="direction" value="' + str(data.direction) + '"></p>\
        <p>Driving time : <input type="number" name="drivingTime"></p>\
        <input type="submit" name="cmd" value="3"> Leave\
      </form>\
    </body>\
  </html>'
  return html