import os

from dotenv import load_dotenv

from autogonai.constants import function_codes as fc
from autogonai.core import Client

load_dotenv()

API_KEY = os.environ.get("API_KEY")

client = Client(api_key=API_KEY)

project = client.Projects.create("Test Name", "Test Description")

print("Inputting data")

data_input = client.Blocks.new(
    function_code=fc.DataInput, project_id=project["id"], id=1
)
data_input.set_params(
    file_type="csv",
    dburl="https://raw.githubusercontent.com/The-Vheed/polygon-datasets/main/mobile_price_prediction.csv",
)
response = data_input.run()
print("Data Input Response:", response, "\n\n")

print(data_input)
# Dropping columns
print("Dropping unnecessary columns")
column_dropping = client.Blocks.new(
    fc.DropColumns,
    project_id=project["id"],
    id=data_input + 1,
    parent=data_input,
)
column_dropping.set_params(d_columns=[0, 1, 3, 8])
response = column_dropping.run()
print("Drop Columns Response:", response, "\n\n")

# Handling missing data
print("Handling missing data from specified columns")
missing_data_handler = client.Blocks.new(
    function_code=fc.HandleMissingData,
    project_id=project["id"],
    id=column_dropping + 1,
    parent=column_dropping,
)
missing_data_handler.set_params(strategy_value="mean", boundaries=":, 2:")
response = missing_data_handler.run()
print("Handling Missing Data Response:", response, "\n\n")

# Encode Data
print("Encoding data")
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
print("Data Encoding Response:", response, "\n\n")

# Feature Sampling
print("Feature Sampling")
feature_sampler = client.Blocks.new(
    function_code=fc.FeatureSampling,
    project_id=project["id"],
    id=data_encoder + 1,
    parent=data_encoder,
)
feature_sampler.set_params(
    x_boundaries=":, :-1",
    y_boundaries=":, -1",
)
response = feature_sampler.run()
print("Feature Sampling Response:", response, "\n\n")

# Splitting Data
print("Splitting Data")
data_splitter = client.Blocks.new(
    function_code=fc.DataSplitting,
    project_id=project["id"],
    id=feature_sampler + 1,
    parent=feature_sampler,
)
data_splitter.set_params(test_size=0.2, random_state=0)
response = data_splitter.run()
print("Splitting Data Response:", response, "\n\n")

# ANN Inititialization
print("ANN Inititialization")
ann_init = client.Blocks.new(
    function_code=fc.ArtificialNeuralNetworkInit,
    project_id=project["id"],
    id=data_splitter + 1,
    parent=data_splitter,
)
ann_init.set_params(
    layer_list=[
        {"type": "dense", "units": 64, "activation": "tanh"},
        {"type": "dense", "units": 64, "activation": "relu"},
        {"type": "dense", "units": 1, "activation": "sigmoid"},
    ]
)
response = ann_init.run()
print("ANN Initialization Response:", response, "\n\n")

# ANN Training
print("ANN Training")
ann_train = client.Blocks.new(
    function_code=fc.ArtificialNeuralNetworkTrain,
    project_id=project["id"],
    id=ann_init + 1,
    parent=ann_init,
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
print("ANN Training Response:", response, "\n\n")

# ANN Evaluation
print("ANN Evaluation")
ann_eval = client.Blocks.new(
    function_code=fc.ArtificialNeuralNetworkEvaluate,
    project_id=project["id"],
    id=ann_train + 1,
    parent=ann_train,
)
ann_eval.set_params(
    hyp_params={"batch_size": 12, "epochs": 5},
)
response = ann_eval.run()
print("ANN Evaluation Response:", response, "\n\n")

# ANN Predict
print("ANN Predict")
ann_pred = client.Blocks.new(
    function_code=fc.ArtificialNeuralNetworkPredict,
    project_id=project["id"],
    id=ann_train + 1,
    parent=ann_train,
)
ann_pred.set_params(
    hyp_params={"batch_size": 12, "epochs": 5},
)
response = ann_pred.run()
print("ANN Predict Response:", response, "\n\n")
