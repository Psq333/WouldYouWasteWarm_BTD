

from machine import Pin, ADC
from time import sleep
import urequests

pot = ADC(Pin(36))

max_scale = 180
max_board_value = 1024

temp_last = 0
temp = 0

stuff = 'home1_internal_temp'
url = 'http://192.168.137.100:8081/'

def send_working_information(infotmation):
  json_string = {'key' : stuff, 'value': infotmation}
  print(json.dumps(json_string).encode('utf-8'))
  response = urequests.post(url,data=json.dumps(json_string).encode('utf-8'))
  response.close()

def start():
  while True:
    pot_value = pot.read()
    tvolt = pot_value * 4.4 / 4095.0
    tempC = (tvolt - 0.5) * 100
    print(pot_value, "  ", tvolt, "  ", tempC)
  
    if int(temp_last) != int(tempC):
      temp_last = tempC
      send_working_information(temp)
  
    print(tempC)
    sleep(5) 




