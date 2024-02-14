import os
from dotenv import load_dotenv

from autogonai.core import Client
from autogonai.constants import function_codes as fc

from PIL import Image

load_dotenv()

API_KEY = os.environ.get("API_KEY")
print("API KEY:", API_KEY)

client = Client(api_key=API_KEY)

response = client.Production.run_pipeline(
    flow_id="fl-sy3bgqa5tdtestestestestestestest",
    data="https://github.com/autogoninc/autogon-public-datasets/raw/main/credit-risk/sample_pred.csv",
)
