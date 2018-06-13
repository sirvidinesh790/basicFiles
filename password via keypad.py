import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False) 

MATRIX = [ [1,2,3],
           [4,5,6],
           [7,8,9],
           ['*',0,'#']]

ROW =   [37,35,33,31]
COL = [29,23,21]

for j in range(3):
    GPIO.setup(COL[j],GPIO.OUT)
    GPIO.output(COL[j],1)

for i in range (4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
def keypad():
    for j in range (3):
            GPIO.output(COL[j],0)

            for i in range(4):
                if GPIO.input (ROW[i]) == 0:
                    print MATRIX[i][j]
                    time.sleep(1)
                    return MATRIX[i][j]
                   

            GPIO.output(COL[j],1)
    
    return "Nothing"
try:
    while(True):
        print keypad()
        
except KeyboardInterrupt:
    GPIO.cleanup()
