import serial


srl = ""


def setup_serial():
    ports = list(serial.tools.list_ports.comports())
    port = ""
    if len(ports) > 1:
        print("Pick port:")
        for p in ports:
            print(p)
        port = ports[int(input("Which one? "))]
    else:
        port = ports[0]
    try:
        srl = serial.Serial(port=port.device)
    except:
        return


def commit(state):
    srl.open()
    srl.write(state)
    srl.close()
