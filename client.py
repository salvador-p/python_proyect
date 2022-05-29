from http import client
from random import randint
from wsgiref import headers
from Iiot_device import Sensor
import json


# Creacion de un objeto de la clase HTTPConnection
_conn = client.HTTPConnection('localhost', port=5000)

# Creacion de un objeto de la clase Sensor

s = Sensor()
h = {'Content-type':'application/json'}
while True:
    z = randint(0,30)
    data = {
        'id':1,
        'name':'Temp sensor',
        'value': z
    }
    json_data = json.dumps(data)

    #print(s.get_temp())
    _conn.request('POST', '/devices', json_data, headers=h)
    _conn.close()
    if(z >= 15):
        print("La inclinacion es de "+ str(z) +"° se necesita atencion")
        print()





        

    
    
