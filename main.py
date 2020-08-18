from web_scraper import *
from serial_comms import *


state = parse_state(get_state())
commit(state)