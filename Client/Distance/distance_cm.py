from hcsr04 import HCSR04

sensor = HCSR04(trigger_pin = 12, echo_pin = 36)

def get_distance:
  distance = sensor.distance_cm()
  print("Distance: ", distance, " cm")
  if distance < 5: #window is close
    return 0
  else:
    return 1
  

