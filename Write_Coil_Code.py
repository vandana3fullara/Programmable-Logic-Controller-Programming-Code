from pyModbusTCP.client import ModbusClient

# Define Your Connection Credential
plc_ip = "192.168.0.5"  # PLC IP
plc_port = 502           # TCP PORT

# Create A Modbus Client
client = ModbusClient(host=plc_ip, port=plc_port)

# Open The Connection
if client.open():
    # Define The Coil Address You Want To Write To
    coil_address = 2048  # Replace With Your Desired Coil Address

    # Define The Value You Want To Write To The Coil (0 For OFF, 1 For ON)
    value_to_write = 1  # Replace With Your Desired Value (0 Or 1)

    # Write A Single Coil
    result = client.write_single_coil(coil_address, value_to_write)

    if result:
        print("Successfully Wrote {} To Coil {}".format(value_to_write, coil_address))
    else:
        print("Failed To Write To Coil")

    # Close The Connection
    client.close()
else:
    print("Failed To Connect")
