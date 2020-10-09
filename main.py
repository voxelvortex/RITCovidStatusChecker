"""
Author: Michael Scalzetti (github.com/voxelvortex)
main.py

This file serves as the main logic that runs everything.
"""
from web_scraper import *
from serial_comms import *
import time


def main():
    srl = setup_serial()
    while 1:
        try:
            state = parse_state(get_state_bsre())
            commit(state, srl)
            time.sleep(3600)
        except Exception as e:
            print("An error occurred, waiting a few seconds and trying again")
            time.sleep(30)


if __name__ == "__main__":
    main()
