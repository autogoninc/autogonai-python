import os
from autogonai.constants import function_codes as fc
#from dotenv import load_dotenv

from autogonai.core import Client

#load_dotenv()

API_KEY = os.environ.get("AUTOGON_API_KEY")

# Driver Code
client = Client(api_key='uCYMpWJL.7KwWPcYNa24EtKMmVr0ZEO7cDXdUJOt7')

project_object= client.Projects.get(
    '722086dd-eda0-4bf7-9ebe-8f38d2dd3ac9'
)

#print(project_object)
'''
with open('uuid.txt', 'w+') as f:
    f.write(project_object['app_id'])
'''
# data_input = client.Blocks.new(function_code=fc.InputData, project=project_object, id=1)
# data_input.set_params(
#     file_type="csv",
#     dburl="https://raw.githubusercontent.com/The-Vheed/polygon-datasets/main/mobile_price_prediction.csv",
#     x_boundaries=":, :-1",
#     y_boundaries=":, -1",
# )
# response = data_input.run()
# print("Data Input Response:", response, "\n\n")
# print(data_input)

# Parameters for a Simple Linear Model
simpleLinear = client.Blocks.new(function_code=fc.SimpleLinearRegression, project=project_object, id=1)
simpleLinear.set_params(
     model_name="helloworld"
 )

response_simpleLinear = simpleLinear.run()

# Parameters for a Simple Linear Model Prediction
simpleLinearPred = client.Blocks.new(function_code=fc.SimpleLinearRegressionPredict, project=project_object, id=1)
simpleLinearPred.set_params(
     model_name="helloworld",
     test_data = " "
 )
response_simpleLinearPred = simpleLinearPred.run()

# Parameters for a Multiple Linear Model
multipleLinear = client.Blocks.new(function_code=fc.MultipleLinearRegression, project=project_object, id=1)
multipleLinear.set_params(
     model_name="helloworld"
 )

response_multipleLinear = multipleLinear.run()

# Parameters for a Multiple Linear Model Prediction
multipleLinearPred = client.Blocks.new(function_code=fc.MultipleLinearRegressionPredict, project=project_object, id=1)
multipleLinearPred.set_params(
     model_name="helloworld",
     test_data = " "
 )

response_multipleLinearPred = multipleLinearPred.run()

# Parameters for a Polynomial Linear Model
polynomialLinear = client.Blocks.new(function_code=fc.PolynomialLinearRegression, project=project_object, id=1)
polynomialLinear.set_params(
     model_name="helloworld",
     degree = 2
 )

response_polynomialLinear = polynomialLinear.run()

# Parameters fpr a Polynomial Linear Model Prediction
polynomialLinearPred = client.Blocks.new(function_code=fc.PolynomialLinearRegressionPredict, project=project_object, id=1)
polynomialLinearPred.set_params(
     model_name="helloworld",
     test_data = " "
 )
response_polynomialLinearPred = polynomialLinearPred.run()

# Parameters for a Support Vector Model
supportVector = client.Blocks.new(function_code=fc.SupportVectorRegression, project=project_object, id=1)
supportVector.set_params(
     model_name="helloworld",
     kernel= "rbf"
 )
response_supportVector = supportVector.run()

# Parameters for a Support Vector Model Prediction
supportVectorPred = client.Blocks.new(function_code=fc.SupportVectorRegressionPredict, project=project_object, id=1)
supportVectorPred.set_params(
     model_name="helloworld",
     test_data = " "
 )
response_supportVectorPred = supportVector.run()

# Parameters for a Decision Tree Model
decisionTree = client.Blocks.new(function_code=fc.DecisionTreeRegression, project=project_object, id=1)
decisionTree.set_params(
     model_name="helloworld",
     random_state = 0
 )
response_decisionTree = decisionTree.run()

# Parameters for a Decision Tree Model Prediction
decisionTreePred = client.Blocks.new(function_code=fc.DecisionTreeRegressionPredict, project=project_object, id=1)
decisionTreePred.set_params(
     model_name="helloworld",
     test_data = " "
 )
response_decisionTreePred = decisionTreePred.run()

# Parameters for a Random Forest Model
randomForest = client.Blocks.new(function_code=fc.RandomForestRegression, project=project_object, id=1)
randomForest.set_params(
     model_name="helloworld",
     random_state = 0,
     n_estimator = 100
 )
response_randomForest = randomForest.run()

# Parameters for a Random Forest Model Prediction
randomForestPred = client.Blocks.new(function_code=fc.RandomForestRegressionPredict, project=project_object, id=1)
randomForestPred.set_params(
     model_name="helloworld",
     test_data = " "
 )
response_randomForestPred = randomForestPred.run()

# Parameters for a Logistic Regression Model 
logisticReg = client.Blocks.new(function_code=fc.LogisticRegression, project=project_object, id=1)
logisticReg.set_params(
     model_name="helloworld",
     random_state = 0
 )
response_logisticReg = logisticReg.run()

# Parameters for a Logistic Regression Model Prediction
logisticRegPred = client.Blocks.new(function_code=fc.LogisticRegressionPredict, project=project_object, id=1)
logisticRegPred.set_params(
     model_name="helloworld",
     test_data = " "
 )
response_logisticRegPred = logisticRegPred.run()

# Parameters for a KNearestNeighbors Model
kNearestN = client.Blocks.new(function_code=fc.KNearestNeighbors, project=project_object, id=1)
kNearestN.set_params(
     model_name="helloworld",
     random_state = 0,
     n_neighbors = 5,
     distance = "minkowski",
     p = 2
 )
response_kNearestN = kNearestN.run()

# Parameters for a KNearestNeighbors Model Prediction
kNearestNPred = client.Blocks.new(function_code=fc.KNearestNeighborsPredict, project=project_object, id=1)
kNearestNPred.set_params(
     model_name="helloworld",
     test_data = " "
 )
response_kNearestNPred = kNearestNPred.run()

# Parameters for a Support Vector Machine Model
supportVectorMachine = client.Blocks.new(function_code=fc.SupportVectorMachine, project=project_object, id=1)
supportVectorMachine.set_params(
     model_name="helloworld"
 )
response_supportVectorMachine = supportVectorMachine.run()

# Parameters for a Support Vector Machine Model Prediction
supportVectorMachinePred = client.Blocks.new(function_code=fc.SupportVectorRegressionPredict, project=project_object, id=1)
supportVectorMachinePred.set_params(
     model_name="helloworld",
     test_data = " "
 )
response_supportVectorMachinePred = supportVectorMachinePred.run()

# Parameters for a Kernel Support Vector Machine Model
kernelSupportVectorMachine = client.Blocks.new(function_code=fc.KernelSupportVectorMachine, project=project_object, id=1)
kernelSupportVectorMachine.set_params(
     model_name="helloworld",
     kernel = "rbf",
     random_state = 0
 )
response_kernelSupportVectorMachine = kernelSupportVectorMachine.run()

# Parameters for a Kernel Support Vector Machine Model Prediction
kernelSupportVectorMachinePred = client.Blocks.new(function_code=fc.KernelSupportVectorMachinePredict, project=project_object, id=1)
kernelSupportVectorMachinePred.set_params(
     model_name="helloworld",
     test_data = " "
 )
response_kernelSupportVectorMachinePred = kernelSupportVectorMachinePred.run()

# Parameters for a Naive Bayes Model
naiveBayes = client.Blocks.new(function_code=fc.NaiveBayes, project=project_object, id=1)
naiveBayes.set_params(
     model_name="helloworld"
 )
response_naiveBayes = naiveBayes.run()

# Parameters for a Naive Bayes Model Prediction
naiveBayesPred = client.Blocks.new(function_code=fc.NaiveBayesPredict, project=project_object, id=1)
naiveBayesPred.set_params(
     model_name="helloworld",
     test_data = " "
 )
response_naiveBayesPred = naiveBayesPred.run()

# Parameters for a Decision Tree Classification Model
decisionTreeClass = client.Blocks.new(function_code=fc.DecisionTreeClassification, project=project_object, id=1)
decisionTreeClass.set_params(
     model_name="helloworld",
     criterion = "gini",
     random_state = 0
 )
response_decisionTreeClass = decisionTreeClass.run()

# Parameters for a Decision Tree Classification Model Prediction
decisionTreeClassPred = client.Blocks.new(function_code=fc.DecisionTreeClassificationPredict, project=project_object, id=1)
decisionTreeClassPred.set_params(
     model_name="helloworld",
     test_data = " "
 )
response_decisionTreeClassPred = decisionTreeClassPred.run()

# Parameters for a Random Forest Classification Model
randomForestClass = client.Blocks.new(function_code=fc.RandomForestClassification, project=project_object, id=1)
randomForestClass.set_params(
     model_name="helloworld"
 )
response_randomForestClass = randomForestClass.run()

# Parameters for a Random Forest Classification Model Prediction
randomForestClassPred = client.Blocks.new(function_code=fc.RandomForestClassificationPredict, project=project_object, id=1)
randomForestClassPred.set_params(
     model_name="helloworld",
     test_data =" "
 )
response_randomForestClassPred = randomForestClassPred.run

# Parameters for a Hierarchical Clustering Model
hierarchicalClust = client.Blocks.new(function_code=fc.HierarchicalClustering, project=project_object, id=1)
hierarchicalClust.set_params(
     model_name="helloworld",
     n_clusters = 5,
     affinity = "euclidean",
     linkage = "ward"
 )
response_hierarchicalClust = hierarchicalClust.run()

# Parameters for a Hierarchical Clustering Model Prediction
hierarchicalClustPred = client.Blocks.new(function_code=fc.HierarchicalClusteringPredict, project=project_object, id=1)
hierarchicalClustPred.set_params(
     model_name="helloworld",
    test_data = " "
 )
response_hierarchicalClustPred = hierarchicalClustPred.run()

# Parameters for a KMeans Clustering Model
kMeansClust = client.Blocks.new(function_code=fc.KMeansClustering, project=project_object, id=1)
kMeansClust.set_params(
     model_name = "helloworld",
     n_clusters = 11,
     init = "k-means++",
     random_state = 42
 )
response_kMeansClust = kMeansClust.run()

# Parameters for a KMeans Clustering Model Prediction
kMeansClustPred = client.Blocks.new(function_code=fc.KMeansClusteringPredict, project=project_object, id=1)
kMeansClustPred.set_params(
     model_name = "helloworld",
    test_data = " "
 )
response_kMeansClustPred = kMeansClustPred.run()

# Parameters for a XGBoost Model
xgBoost = client.Blocks.new(function_code=fc.XGBoost, project=project_object, id=1)
xgBoost.set_params(
     model_name = "helloworld"
 )
response_xgBoost = xgBoost.run()

# Parameters for a XGBoost Model Prediction
xgBoostPred = client.Blocks.new(function_code=fc.XGBoostPredict, project=project_object, id=1)
xgBoostPred.set_params(
     model_name = "helloworld",
     test_data = " "
 )
response_xgBoost = xgBoostPred.run()

