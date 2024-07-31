from pyModbusTCP.client import ModbusClient
import struct

# Define Connection Credential Here
plc_ip = "192.168.0.5"  
plc_port = 502           

# Create A Modbus Client
client = ModbusClient(host=plc_ip, port=plc_port)

# Open The Connection 
if client.open():
    # Define The Starting Register Address For The Float Value
    register_address = 4196  # Replace With Your Desired Starting Register Address

    # Define The Floating Point Value You Want To Write
    value_to_write = 123.45  # Replace With Your Desired Float Value

    # Convert The Float Value To A Bytes Object (4 Bytes)
    float_bytes = struct.pack('>f', value_to_write)

    # Unpack The Bytes Object Into Two 16-Bit Integers (Words)
    float_words = struct.unpack('>HH', float_bytes)

    # Write The Two Words To Consecutive Registers
    result = client.write_multiple_registers(register_address, float_words)

    if result:
        print("Successfully Wrote {} To Registers {} And {}".format(
            value_to_write, register_address, register_address + 1))
    else:
        print("Failed To Write Float Value To Registers")

    # Close The Connection
    client.close()
else:
    print("Failed To Connect")
