## AutogonAI Python Library Readme

### Overview

The AutogonAI Python library is a tool for interacting with AutogonAI's AI automation platform. It enables you to build and manage machine learning projects using a variety of functions and APIs provided by AutogonAI. With this library, you can streamline your machine learning workflow and take advantage of AutogonAI's automation capabilities.

### Installation

You can install the AutogonAI Python library using pip:

```bash
pip install autogonai
```


### Getting Started

To begin using the AutogonAI Python library, you need an API key, which you can obtain from AutogonAI. Once you have your API key, you can set it as an environment variable or pass it directly to the Client object.

```python
import os
from dotenv import load_dotenv
from autogonai.constants import function_codes as fc
from autogonai.core import Client

load_dotenv()

API_KEY = os.environ.get("API_KEY")

client = Client(api_key=API_KEY)
```

### Example Usage

Here's an example of how to use the AutogonAI Python library to create a machine learning project and perform various data preprocessing and training tasks:

```python
# Create a new project
project = client.Projects.create("Test Name", "Test Description")

# Data Input
data_input = client.Blocks.new(
    function_code=fc.DataInput,
    project_id=project["id"],
    id=1
)
data_input.set_params(
    file_type="csv",
    dburl="https://raw.githubusercontent.com/The-Vheed/polygon-datasets/main/mobile_price_prediction.csv",
)
response = data_input.run()

# Drop Columns
column_dropping = client.Blocks.new(
    fc.DropColumns,
    project_id=project["id"],
    id=data_input + 1,
    parent=data_input,
)
column_dropping.set_params(d_columns=[0, 1, 3, 8])
response = column_dropping.run()

# Handle Missing Data
missing_data_handler = client.Blocks.new(
    function_code=fc.HandleMissingData,
    project_id=project["id"],
    id=column_dropping + 1,
    parent=column_dropping,
)
missing_data_handler.set_params(strategy_value="mean", boundaries=":, 2:")
response = missing_data_handler.run()

# Encode Data
data_encoder = client.Blocks.new(
    function_code=fc.DataEncoding,
    project_id=project["id"],
    id=missing_data_handler + 1,
    parent=missing_data_handler,
)
data_encoder.set_params(
    dataset={
        "encode": True,
        "encoding_type": "label",
        "remainder": "passthrough",
        "index": 1,
    }
)
response = data_encoder.run()

# ... Continue with other data processing tasks

# Train an Artificial Neural Network (ANN)
ann_train = client.Blocks.new(
    function_code=fc.ArtificialNeuralNetworkTrain,
    project_id=project["id"],
    id=data_encoder + 1,
    parent=data_encoder,
)
ann_train.set_params(
    model_name="titanic model",
    hyp_params={
        "optimizer": "adam",
        "loss": "binary_crossentropy",
        "metrics": ["accuracy"],
        "batch_size": 12,
        "epochs": 5,
    },
)
response = ann_train.run()

# ... Continue with evaluation and prediction
```


This is just a basic example to demonstrate how to use the AutogonAI Python library. You can customize it to suit your specific machine learning project requirements.

### Production Pipelines

You can also use the AutogonAI Python library to make pipeline predictions in production. Here's an example of how to call a production machine learning predict pipeline:

```python
response = client.Production.run_pipeline(
    flow_id="fl-sy3bgqa5tdtestestestestestestest",
    data="https://github.com/autogoninc/autogon-public-datasets/raw/main/credit-risk/sample_pred.csv",
)
```

### Additional AutogonAI APIs

AutogonAI also provides additional APIs like 'Qore' APIs for image functions like 'Image generation' and others.
Here's an example on image generation:
```python
response = client.Qore.VisionAI.image_generation(
    "A dad and his son walking down the street towards a park", "512x512"
)

image = Image.open(response["image"])
image.show()
```
Output:

![Image of a dad and his son walking down the street towards a park](tests/showcase.PNG)

### Documentation

For detailed documentation and usage instructions, please refer to [AutogonAI's official API documentation](https://docs.autogon.ai/)
.

### Support

If you encounter any issues or have questions about the AutogonAI Python library or AutogonAI's platform, please [contact us](https://autogon.ai/company/contact) directly, or raise the issue up on our [discord server](https://discord.gg/3NhD8mcq5F)