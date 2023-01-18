class Sensor:
    def __init__(self, numSens):
        self.numSens = numSens

    def read_file(self):
        try:
            entrada = input('ingrese temp para sensor de temperatura o hum para el sensor de humedad: ')
            assert self.numSens < 3 and (entrada == 'temp' or entrada == 'hum')
            archivo = open(f'{entrada}{self.numSens}.txt', 'rt')
            linea = archivo.readline()
            while linea:
                sensor, valor = linea.split(';')
                valor = valor.rstrip('\n')
                if int(sensor) == self.numSens:
                    break
                linea = archivo.readline()
            print('archivo leido correctamente')
            return float(valor)
        except AssertionError:
            return 'Error: el sensor no existe'
        except OSError:
            return ('El programa no puede leer el archivo')

    @staticmethod
    def get_value():
        return 0

class SensorTemperatura(Sensor): 
    def __init__(self, numSens):
        super().__init__(numSens)

    def get_value(self):
        if super().read_file() > 0:
            return super().read_file()
        else:
            return super().get_value()
       
        
class SensorHumedad(Sensor):
    def __init__(self, numSens ):
        super().__init__(numSens)
    
    def get_value(self):
        return super().read_file()/10

primersensor = SensorHumedad(0)

print(primersensor.get_value())



