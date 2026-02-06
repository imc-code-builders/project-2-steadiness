from microbit import *
import log

log.set_labels('x', 'y', 'z')
logging = False
display.show(Image.NO)
while True:

    if button_a.was_pressed():
        if logging:
            logging = False
            display.show(Image.NO)
            sleep(400)
        else:
            logging = True
            display.show(Image.YES)
            sleep(400)

    if button_b.was_pressed():
        log.delete()

    if logging:
        log.add({
            'x': accelerometer.get_x(),
            'y': accelerometer.get_y(),
            'z': accelerometer.get_z()
        })
        sleep(100)

