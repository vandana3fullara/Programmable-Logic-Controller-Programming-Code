from pyModbusTCP.client import ModbusClient
import struct

# Define Your Connection Credentials Here
plc_ip = "192.168.0.5"  
plc_port = 502          

# Create A Modbus Client
client = ModbusClient(host=plc_ip, port=plc_port)

# Open The Connection 
if client.open():
    # Define The Register Address You Want To Read
    register_address = 4097  # Replace With Your Desired Register Address

    # Read A Single Holding Register
    result = client.read_holding_registers(register_address, 2)

    if result:
        # Print The Value Read From The Register
        float_value = struct.unpack('>f', struct.pack('>HH', *result))[0]
        print("Float Value In Registers {}: {}".format(register_address, float_value))
    else:
        print("Failed To Read Register")

    # Close The Connection
    client.close()
else:
    print("Failed To Connect")

