import picoweb
import json
import mqtt
import screen

from time import sleep
import station_mode

def list_json(j_data):
  fields_data= {
    'field1' : 0,
    'field2' : j_data['home1_external_temp'],
    'field3' : j_data['home1_internal_temp'],
    'field4' : j_data['home1_room1_radiator1'],
    'field5' : j_data['home1_room1_radiator2'],
    'field6' : j_data['home1_room1_window1'],
    'field7' : j_data['home1_room1_window2'],
    'field8' : j_data['home1_room1_window3']
  }
  return fields_data 

  
screen.scritturaD()
ip = station_mode.connection()                  # store the IP address 
sleep(1)


j_data = {
  'home1_external_temp' : 25,
  'home1_internal_temp' : 35,
  'home1_room1_radiator1' : 0,
  'home1_room1_radiator2' : 0,
  'home1_room1_window1' : 0,
  'home1_room1_window2' : 0,
  'home1_room1_window3' : 0}
sleep(1)
screen.scrittura(ip, j_data,False)
app = picoweb.WebApp(__name__)            # create server

@app.route('/')                           
def index(req, resp):
  method = req.method 
  
  if method == 'GET':
    encoded = json.dumps(j_data)         
    yield from picoweb.start_response(resp, content_type = "application/json")
    yield from resp.awrite(encoded)     
  
  elif method == 'POST':
    yield from req.read_form_data() 
    body = req.form
    sleep(0.5)
    for key, value in body.items():
      tmp = key
    tmp = "".join(tmp.split()).replace(" ","") 
    body_parsed = json.loads(tmp) 
    print(body_parsed)
    j_data[body_parsed['key']] = body_parsed['value'] 

    yield from picoweb.start_response(resp,content_type = "application/json")
    yield from resp.awrite(json.dumps(j_data))
    screen.scrittura(ip, j_data,True)
    for i in range(0,15):
      mqtt.CollegamentoMQTT("WADO64OYOU9S6QVY", list_json(j_data))
    screen.scrittura(ip, j_data,False)
    sleep(2)
app.run(debug=True, host =ip)

