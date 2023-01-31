import pyb


class MotorDriver:
    """!
    This class implements a motor driver for an ME405 kit.
    """

    def __init__(self, en_pin, in1pin, in2pin, timer):
        """!
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety.
        @param en_pin (There will be several pin parameters)
        """
        print("Creating a motor driver")
        self.enable_pin = en_pin
        self.enable_pin.init(pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)
        self.enable_pin.high()
        self.input1pin = in1pin
        self.input1pin.init(pyb.Pin.OUT_PP)
        self.input2pin = in2pin
        self.input2pin.init(pyb.Pin.OUT_PP)
        self.motortimer = pyb.Timer(timer, freq=20000)
        self.CCW = self.motortimer.channel(1, pyb.Timer.PWM, pin=in1pin)
        self.CW = self.motortimer.channel(2, pyb.Timer.PWM, pin=in2pin)

    def set_duty_cycle(self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor
        """
        print(f"Setting duty cycle to {level}")
        if level > 100:
            level = 100
        elif level < -100:
            level = -100
        if -100 <= level < 0:
            self.CW.pulse_width_percent(-level)
            self.CCW.pulse_width_percent(0)
        elif 0 < level <= 100:
            self.CW.pulse_width_percent(0)
            self.CCW.pulse_width_percent(level)
        else:
            self.CW.pulse_width_percent(0)
            self.CCW.pulse_width_percent(0)


if __name__ == '__main__':
    motor1 = MotorDriver(pyb.Pin.cpu.A10, pyb.Pin.cpu.B4, pyb.Pin.cpu.B5, 3)
    motor1.set_duty_cycle(100)
