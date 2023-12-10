from pyModbusTCP.client import ModbusClient

# Create An Instance Of ModbusClient (This Is Needed To Access The Methods)
dummy_client = ModbusClient()

# Get A List Of All Attributes (Including Methods) Of ModbusClient
all_attributes = dir(dummy_client)

# Filter The List To Only Include Methods (Functions)
methods_only = [attr for attr in all_attributes if callable(getattr(dummy_client, attr))]

# Print The List Of Methods
for method_name in methods_only:
    print(method_name)
