import network
import urequests          # library used for making HTTP requests
import time
import json
import mydistance_cm

stuff = 'home1_room1_window1'  #name of device
value = 0
url = 'http://192.168.137.252:8081/'  #Server IP

while True:
  change = mydistance_cm.get_distance()
  if change != value:
    value = int(change)
    json_string = {'key' : stuff, 'value': value}
    print(json.dumps(json_string).encode('utf-8'))
    response = urequests.post(url,data=json.dumps(json_string).encode('utf-8'))
    response.close()
  time.sleep(1)
