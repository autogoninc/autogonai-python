import os

from dotenv import load_dotenv

from autogonai.core import Base

load_dotenv()

API_KEY = os.environ.get("AUTOGON_API_KEY")

# Driver Code
client = Base()
project_object: dict = client.Project.create(
    "Project #0", "This is a short description for my first project"
)
