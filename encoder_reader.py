import pyb


class EncoderReader:
    def __init__(self, pinA, pinB, timer):
        self.pinA = pinA
        self.pinB = pinB
        self.encodertimer = pyb.Timer(timer, prescaler=0, period=65535)
        self.ch1 = self.encodertimer.channel(1, pyb.Timer.ENC_AB, pin=self.pinA)
        self.ch2 = self.encodertimer.channel(2, pyb.Timer.ENC_AB, pin=self.pinB)
        self.delta = 0
        self.initialCount = 0
        self.count = 0
        self.position = 0

    def update(self):
        self.initialCount = self.count
        self.count = self.encodertimer.counter()
        self.delta = self.count-self.initialCount
        self.initialCount = self.count
        if self.delta >= 65535/2:
            self.delta -= 65535
        elif self.delta <= -65535/2:
            self.delta += 65535
        self.position += self.delta

    def read(self):
        self.update()
        print(self.position, '\r')
        return self.position, self.delta

    def zero(self):
        self.delta = 0
        self.initialCount = 0
        self.count = 0
        self.position = 0

    def set(self, position):
        self.position = position
        self.delta = 0
