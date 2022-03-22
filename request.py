import re

def parse(request):

  cmd = 0
  drivingTime = 0
  smallCoefficient = 0
  largeCoefficient = 0
  maxDuty_ns = 0

  result = re.search(r'favicon.ico', request)

  if result != None:
    return (
      cmd, 
      drivingTime, 
      smallCoefficient, 
      largeCoefficient, 
      maxDuty_ns
    )

  result = re.search(r'cmd=[a-z]*', request)

  if result != None:
    if result.group(0) == 'cmd=calibrate':
      cmd = 1
    elif result.group(0) == 'cmd=set':
      cmd = 2
    elif result.group(0) == 'cmd=drive':
      cmd = 3
      result = re.search(r'driving_time=(\d*)', request)
      result = re.search(r'\d+$', result.group(0))
      drivingTime = int(result.group(0))

      result = re.search(r'small_coefficient=(\d*)', request)
      result = re.search(r'\d+$', result.group(0))
      smallCoefficient = int(result.group(0))

      result = re.search(r'large_coefficient=(\d*)', request)
      result = re.search(r'\d+$', result.group(0))
      largeCoefficient = int(result.group(0))

      result = re.search(r'max_duty_ns=(\d*)', request)
      result = re.search(r'\d+$', result.group(0))
      maxDuty_ns = int(result.group(0))
    elif result.group(0) == 'cmd=stop':
      cmd = 4

  return (
      cmd, 
      drivingTime, 
      smallCoefficient, 
      largeCoefficient, 
      maxDuty_ns
    )