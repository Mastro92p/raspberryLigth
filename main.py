import sys, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)


def main():
    while True:
        print(GPIO.input(4))

if __name__ == '__main__':
    main()
