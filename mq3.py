import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # This command is to Disable Warning....!!!!

MQ_3 = 21
buzzer = 20
GPIO.setup(21, GPIO.IN)
GPIO.setup(20, GPIO.OUT)
import sys
import urlopen
import urllib

from time import sleep
# Enter Your API key here
User1API = '90ZTHLRU35UTOEO8' 

# URL where we will send the data, Don't change it
baseURL1 = 'https://api.thingspeak.com/update?api_key=%s' % User1API
while True:
    j1=GPIO.input(MQ_3)
    print(j1)
    conn = baseURL1 + '&field1=%s' % (j1)
    request = urllib.request.Request(conn)
    responce = urllib.request.urlopen(request)
    responce.close()
    if j1==0 :
        print('Smoke Detected!')
        time.sleep(0.5)
        GPIO.output(20, True)
        time.sleep(0.5)
        GPIO.output(20, False)
       
    else :
        print ('Smoke Not Detected!')
        time.sleep(0.1)
        GPIO.output(20, False)
