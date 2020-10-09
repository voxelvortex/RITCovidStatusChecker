from web_scraper import *
from serial_comms import *
import time


srl = setup_serial()
while 1:
    try:
        state = parse_state(get_state_bsre())
        commit(state, srl)
        time.sleep(3600)
    except Exception as e:
        print("An error occurred, waiting a few seconds and trying again")
        time.sleep(30)
