from pyModbusTCP.client import ModbusClient

# Define Connection Credential Here
plc_ip = "192.168.0.5"  # PLC IP 
plc_port = 502           # TCP PORT

# Create a Modbus Client
client = ModbusClient(host=plc_ip, port=plc_port)

# Open The Connection
if client.open():
    # Define The Register Address You Want To Write To
    register_address = 4100  # Replace With Your Desired Register Address

    # Define The Value You Want To Write To The Register
    value_to_write = 1111  # Replace With Your Desired Value

    # Write A Single Holding Register
    result = client.write_single_register(register_address, value_to_write)

    if result:
        print("Successfully Wrote {} To Register {}".format(value_to_write, register_address))
    else:
        print("Failed To Write To Register")

    # Close The Connection
    client.close()
else:
    print("Failed To Connect")
