from pyModbusTCP.client import ModbusClient

# Define Your Connection Credentals Here
plc_ip = "192.168.0.5"  # PLC IP
plc_port = 502           # TCP PORT

# Create A Modbus Client
client = ModbusClient(host=plc_ip, port=plc_port)

# Open The Connection
if client.open():
    # Define The Register Address You Want To Read
    coil_address = 1280  # Replace With Your Desired Register Address

    # Read A Single Holding Register
    result = client.read_coils(coil_address, 1)

    if result:
        # Print The Value Read From The Register
        print("Value In Register {}: {}".format(coil_address, result[0]))
    else:
        print("Failed To Read Register")

    # Close The Connection
    client.close()
else:
    print("Failed To Connect")

