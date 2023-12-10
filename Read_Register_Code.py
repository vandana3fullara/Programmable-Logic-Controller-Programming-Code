from pyModbusTCP.client import ModbusClient

# Define Here Your Connection Credential
plc_ip = "192.168.0.5"  # PLC IP 
plc_port = 502           # TCP PORT

# Create A Modbus Client
client = ModbusClient(host=plc_ip, port=plc_port)

# Open The Connection
if client.open():
    # Define The Register Address You Want To Read
    register_address = 4096  # Replace With Your Desired Register Address

    # Read A Single Holding Register 
    result = client.read_holding_registers(register_address, 1)

    if result:
        # Print The Value Read From The Register
        print("Value In Register {}: {}".format(register_address, result[0]))
    else:
        print("Failed To Read Register")

    # Close The Connection
    client.close()
else:
    print("Failed To Connect")
