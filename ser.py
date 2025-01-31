import serial.tools.list_ports_windows

ports = serial.tools.list_ports_windows.comports()

for port_info in ports:
    print(port_info.manufacturer)
    
    print("-" * 50)