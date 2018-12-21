
import Adafruit_DHT
sensorHumedity=Adafruit_DHT.DHT11
pin=2
humidity,temperature=Adafruit_DHT.read_retry(sensorHumedity,pin)
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Error como lo que me dijo mi madre al nacer')