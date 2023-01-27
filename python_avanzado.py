'''Se tiene un sistema embebido que posee sensores de temperatura y humedad Mediante servicios
que corren en el sistema, se leen los valores de los sensores y se dejan escritos en archivos que se
encuentran en /tmp con el siguiente formato:
• Sensor de temperatura: /tmp/tempX.data Siendo X el número de sensor.
• Sensor de humedad: /tmp/humX.data Siendo X el número de sensor.
Modelar en un programa en Python los sensores definiendo las siguientes clases:
• Clase “Sensor”: recibe en el constructor el número de sensor. Tiene un método “read_file”
que permite leer un valor float de un archivo. El mismo recibe el path al archivo y devuelve
un float. Tiene un método “get_value()” que devuelve siempre 0.
• Clase “SensorTemperatura”: Hereda de la clase “Sensor”. Tiene un método “get_value()”
que devuelve la temperatura en un float truncando la parte negativa (si es menor que cero
devuelve 0)
• Clase “SensorHumedad”: Hereda de la clase “Sensor”. Tiene un método “get_value()” que
devuelve la humedad leída haciendo un cambio de escala respecto del valor que está en el
archivo: lo divide por 10.
Crear los archivos /tmp/temp0.data , /tmp/temp1.data, /tmp/temp2.data , /tmp/hum0.data ,
/tmp/hum1.data y cargarle valores. Hacer un programa que defina los objetos y llame a los métodos
get_value() para probar el funcionamiento.
'''

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



