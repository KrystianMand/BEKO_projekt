import serial
import requests
from time import sleep
from ast import literal_eval

port = 'COM3' 
baud_rate = 115200 

ser = serial.Serial(port, baud_rate)

res = requests.get('http://192.168.114.185:8000/endpoints/animations/0')

rgb_values = literal_eval(res.json()['rgb_values'])

while True:
    for frame in rgb_values:
        print('NEW FRAME')
        for i in range(16):
            data_to_send = str(frame[16 * i:16 * i + 16]) + '\n'
            data_to_send = data_to_send.replace("[", "").replace("]", "").replace(" ", "")
            print(data_to_send)
            ser.write(data_to_send.encode())
            sleep(0.1)
        # sleep(1)
