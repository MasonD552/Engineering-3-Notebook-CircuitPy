import board 
import adafruit_hcsr04 
from PID_CPY import PID  
import pwmio   
import time 

pid = PID(15000,1.0,4750) # PID parameters
pid.setpoint = 15.00     # setpoint
pid.output_limits = (20000.00,50000.00) # output limits

fanMotor = pwmio.PWMOut(board.D8,duty_cycle = 65535) # fanfanMotor
fanMotor.duty_cycle = 0 

dist = adafruit_hcsr04.HCSR04(trigger_pin = board.D3, echo_pin = board.D2) # distance sensor

while True:
    try:
        height = 26 - dist.distance # 26 is the height of the tower
        speed = int(pid(height))    # pid output
        fanMotor.duty_cycle = speed # fan speed
        print("speed ", speed, " height ", height,)  
    except RuntimeError: 
        print("retry") 
    time.sleep(0.1)     # 0.1 second delay