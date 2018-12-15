
import RPi.GPIO as GPIO

led_state=True
led_pin=23

class GpioSmartMirrorHelpers():
    def initGpio(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(led_pin, GPIO.OUT)
        GPIO.output(led_pin, led_state)

    def changeSMLedState(self):
        global led_state
        led_state = not led_state
        GPIO.output(led_pin, led_state)
    def getSMLedState(self):
        global led_state
        return led_state