import time
#from get_information import whole
import get_information

sleep_time = 1*60*60*24
while True:
    get_information.whole()
    time.sleep(sleep_time)



