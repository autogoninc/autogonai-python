import os
from dotenv import load_dotenv

from autogonai.core import Client
from autogonai.constants import function_codes as fc

from PIL import Image

load_dotenv()

API_KEY = os.environ.get("API_KEY")
print("API KEY:", API_KEY)

client = Client(api_key=API_KEY)

response = client.Qore.VisionAI.image_generation(
    "A dad and his son walking down the street towards a park", "512x512"
)

image = Image.open(client.Qore.VisionAI._process_image_to_bytes(response["image"]))
image.show()
