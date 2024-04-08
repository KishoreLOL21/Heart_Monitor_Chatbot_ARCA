import serial
import serial.tools.list_ports
import smbus2
import time

# Define I2C address for MAX30100
MAX30100_I2C_ADDR = 0x57

# Define registers for MAX30100
MAX30100_REG_INT_STATUS = 0x00
MAX30100_REG_FIFO_DATA = 0x07

# Create an smbus object
bus = smbus2.SMBus(1)  # Use the appropriate bus number for your system

def read_sensor():
    # Read heart rate and SpO2 values
    data = bus.read_i2c_block_data(MAX30100_I2C_ADDR, MAX30100_REG_FIFO_DATA, 4)

    # Convert raw data to heart rate and SpO2 values
    heart_rate = data[3]
    spo2 = data[2]

    return heart_rate, spo2

def arduino():
    ports = serial.tools.list_ports.comports()
    using = None

    # Find the selected port in the list of available ports
    for port in ports:
        if "USB" and "SERIAL" in port.description:
            using = port.device
            print(using)

    # If the selected port is found, configure and open the serial connection
    if using:
        serialinst = serial.Serial(using, 9600)
        try:
            while True:
                message = input("Enter a Message for Arduino: ")
                serialinst.write((message + '\n').encode('utf-8'))  # Send message with a newline character

                if message.upper() == "ON":  # If user inputs "ON"
                    # Read heart rate from sensor
                    heart_rate, spo2 = read_sensor()
                    serialinst.write((f"Heart Rate: {heart_rate}, SpO2: {spo2}\n").encode('utf-8'))  # Send heart rate value to Arduino
                    print("Heart rate value sent to Arduino:", heart_rate)

                choice = input("Shall we continue? (Y/N): ")
                if choice.upper() == "N":
                    serialinst.close()
                    break
        except KeyboardInterrupt:  # Catch Ctrl+C termination
            print("\nTerminating script...")
            serialinst.write("TERMINATE\n".encode('utf-8'))  # Send termination signal
            serialinst.close()
    else:
        print("Selected port not found.")
        
# Main_Program:
        
# Get a list of available COM ports


arduino()
