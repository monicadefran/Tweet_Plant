
import Adafruit_DHT
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["plant"]
mycol = mydb["monitoring"]


sensorHumedity=Adafruit_DHT.DHT11
pin=2

try:
    while True:
        humidity,temperature=Adafruit_DHT.read_retry(sensorHumedity,pin)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
            mydocument = { "temperature": temperature, "humidity": humidity }
            x = mycol.insert_one(mydocument)
        else:
            print('Error como lo que me dijo mi madre al nacer')
except KeyboardInterrupt:
    pass

