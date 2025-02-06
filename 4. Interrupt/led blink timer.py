from machine import Pin, Timer

led = Pin(21, Pin.OUT)    # create output pin on GPIO21

def blink_isr(event):
    if led.value() == False:
        led.on()
    else:
        led.off()

blink_timer = Timer(1)
blink_timer.init(period=250, mode=Timer.PERIODIC, callback=blink_isr)