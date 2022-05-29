from random import randint
import psutil


class Sensor:

    #Constructor de la clase
    def __init__(self):
        self._sensor = psutil.cpu_stats()

    def get_temp(self):
        return self._sensor['coretemp']

    #Simular la toma de algun valor de otro sensor
    def get_random_number(self):
        return randint(0,99)