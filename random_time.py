from time import strftime, sleep

def every_sec():
    x = 0
    while x < 10:
        print strftime("%a, %d %b %Y %H:%M:%S")
        sleep(1)
        x += 1

every_sec()
