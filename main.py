from web_scraper import *
from serial_comms import *
import time


srl = setup_serial()
while 1:
    state = parse_state(get_state())
    commit(state, srl)
    time.sleep(3600)
