import machine
import urequests 

def CollegamentoMQTT(API_Write, fields):
  readings = fields
  HTTP_HEADERS = {'Content-Type': 'application/json'} 
  THINGSPEAK_WRITE_API_KEY = API_Write

  request = urequests.post( 
    'http://api.thingspeak.com/update?api_key=' +
    THINGSPEAK_WRITE_API_KEY, 
    json = readings, 
    headers = HTTP_HEADERS )  
  request.close()
  print("INVIATOOOOOOOOOOOOOOOO")
  print(readings) 
