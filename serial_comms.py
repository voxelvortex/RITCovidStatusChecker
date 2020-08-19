from serial import Serial
from serial.tools import list_ports_windows
import time


def setup_serial():
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
    srl.open()
    time.sleep(2)   # apparently the arduino resets when a new serial link is made using pyserial on windows??
                    # so as a result you have to add a sleep command to wait for the arduino to restart
    print("Sending: {0}".format(state))
    srl.write(str(state).encode())
    srl.close()
