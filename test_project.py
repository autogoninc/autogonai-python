import os
from dotenv import load_dotenv

from autogonai.core import Client
from autogonai.constants import function_codes as fc

load_dotenv()

API_KEY = os.environ.get("AUTOGON_API_KEY")

client = Client(api_key=API_KEY)

print("Inputting data")
data_input = client.Blocks.new(fc.InputData, project_id=8, block_id=1)
data_input.set_params(
    file_type="csv",
    dburl="https://raw.githubusercontent.com/The-Vheed/polygon-datasets/main/mobile_price_prediction.csv",
    x_boundaries=":, :-1",
    y_boundaries=":, -1",
)
response = data_input.run()

# Dropping columns
print("Dropping unnecessary columns")
column_dropping = client.Blocks.new(
    fc.DropColumns, project_id=8, block_id=2, parent_id=1
)
column_dropping.set_params(x_columns=[0, 1, 3, 8], y_columns=None)
column_dropping.run()

# Handling missing data
print("Handling missing data from specified columns")
missing_data_handler = client.Blocks.new(
    function_code=fc.HandleMissingData, project_id=8, block_id=3, parent_id=2
)
print(missing_data_handler.body)