import RPi.GPIO as GPIO    #Imports the needed libraries
import time

GPIO.setwarnings(False)    #Disables the GPIO warnings

LED = 17    #Makes the statement LED mean 17 to the python code

GPIO.setmode(GPIO.BCM)    #You put this before you setup the GPIO pins as inputs or outputs
GPIO.setup(LED, GPIO.OUT)    #Sets the GPIO pin for the led as a output

while True:    #Infinite loop
    GPIO.output(LED, GPIO.HIGH)    #GPIO.HIGH urns on the led by sending power to the GPIO pin
    time.sleep(.5)    #Tells the code to wait .5 seconds before continuing
    GPIO.output(LED, GPIO.LOW)    #GPIO.LOW turns off the led by removing the power going to it
    time.sleep(.5)
    
GPIO.cleanup()     #Cleans up all ports listed
    
