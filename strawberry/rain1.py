from gpiozero import Button
import time

switch = Button(21)

while True:
    if switch.is_pressed:
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("{}, water detected!".format(time_str))
    else:
        pass
    time.sleep(0.2)  # 以每秒5次的频率检测，也就是5Hz检测频率