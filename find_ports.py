import platform
import serial.tools.list_ports

def find_usb_serial_ports():
    """
    Finds and returns a list of serial port names that are likely connected to USB devices.

    Returns:
        A list of strings, where each string is a serial port name (e.g., "COM1", "/dev/ttyUSB0").
        Returns an empty list if no USB serial ports are found.
    """

    ports = serial.tools.list_ports.comports()  # Get all available ports

    usb_ports = []
    for port in ports:
        port_name = port.device  # Get the port name (e.g., "COM1", "/dev/ttyUSB0")
        # Add more robust checks if needed (e.g., check the port description for "USB")
        if platform.system() == "Windows":
          if "COM" in port_name.upper(): #Check if its a COM port on Windows
            usb_ports.append(port_name)
        elif platform.system() == "Linux":
          if "ttyUSB" in port_name or "ttyACM" in port_name: #Check for the usual ttyUSB or ttyACM on Linux
            usb_ports.append(port_name)

    return usb_ports


if __name__ == "__main__":
    usb_serial_ports = find_usb_serial_ports()

    if usb_serial_ports:
        print("USB Serial Ports Found:")
        for port in usb_serial_ports:
            print(port)
    else:
        print("No USB Serial Ports Found.")