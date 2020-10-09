"""
Author: Michael Scalzetti (github.com/voxelvortex)
serial_comms.py

This file contains helper functions that allow the program
to send alert information from RIT's website to an arduino
so that it can display that information.
"""
from serial import Serial
from serial.tools import list_ports_windows
import time


def setup_serial():
    """
    This function sets up a serial.Serial object and returns it.
    It covers potential issues such in the case that there are
    multiple serial devices, it will prompt the user to select
    the on they'd like to use

    :return: serial.Serial object
    """
    ports = list(list_ports_windows.comports())
    port = ""
    if len(ports) > 1:
        print("Pick port:")
        for i in range(len(ports)):
            print("{0}: {1}".format(i + 1, ports[i]))
        port = ports[int(input("Which one? "))-1]
    else:
        port = ports[0]
    try:
        srl = Serial(port=port.device)
        srl.close()
        return srl
    except Exception as e:
        print(e)


def commit(state, srl):
    """
    :param state: int ranging from 0 to 3 (inclusive to inclusive)
                  which represents the current alert level at RIT
    :param srl: serial.Serial object obtained by running setup_serial()

    :return: None
    """
    srl.open()
    time.sleep(2)   # apparently the arduino resets when a new serial link is made using pyserial on windows??
                    # so as a result you have to add a sleep command to wait for the arduino to restart
    print("Sending: {0}".format(state))
    srl.write(str(state).encode())
    srl.close()
