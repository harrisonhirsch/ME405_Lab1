import pyb
import motor_driver
import encoder_reader

"""!
    @file                       main.py
    @brief                      Test if motor_driver.py and encoder_driver.py work
    @details                    This is test file to demonstrate that motor_driver.py and encoder_driver.py work
                                as intended. the main() function that is commented out below was used to make the
                                motor and encoder work before a class was made for them as well as have us learn
                                how to interact with them. We feel its important to show, as well as a good
                                reference for debugging.
                                
    @author                     Peyton Archibald
    @author                     Harrison Hirsch
    @date                       January 31, 2023
"""

# def main():
#     while True:
#         print(tim3.counter())
#
#     pinA10 = pyb.Pin(pyb.Pin.cpu.A10, pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)
#     pinA10.high()
#     # pinC1 = pyb.Pin(pyb.Pin.cpu.C1, pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)
#     pinB4 = pyb.Pin(pyb.Pin.cpu.B4, pyb.Pin.OUT_PP)
#     pinB5 = pyb.Pin(pyb.Pin.cpu.B5, pyb.Pin.OUT_PP)
#     # pinA0 = pyb.Pin(pyb.Pin.cpu.A0, pyb.Pin.OUT_PP)
#     # pinA1 = pyb.Pin(pyb.Pin.cpu.A1, pyb.Pin.OUT_PP)
#     tim3 = pyb.Timer(3, freq=20000)
#     # tim5 = pyb.Timer(5, freq=20000)
#     #     ch1 = tim3.channel(1, pyb.Timer.ENC_AB, pin=pinB6)
#     CW = tim3.channel(1, pyb.Timer.PWM, pin=pinB4)
#     CCW = tim3.channel(2, pyb.Timer.PWM, pin=pinB5)
#     CW.pulse_width_percent(0)
#     CCW.pulse_width_percent(0)


if __name__ == '__main__':
    
    motor1 = motor_driver.MotorDriver(pyb.Pin.cpu.A10, pyb.Pin.cpu.B4, pyb.Pin.cpu.B5, 3)
    motor1.set_duty_cycle(75)
    
    encoder1 = encoder_reader.EncoderReader(pyb.Pin.cpu.C6, pyb.Pin.cpu.C7, 8)
    encoder2 = encoder_reader.EncoderReader(pyb.Pin.cpu.B6, pyb.Pin.cpu.B7, 4)
    while True:
        value1 = encoder1.read()
        value2 = encoder2.read()
