
import time


minut = 0
second = 0

while second < 60:
    print(f'{minut:02}:{second:02}')
    time.sleep(1)
    second += 1
 