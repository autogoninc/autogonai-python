class function_codes:
    # Data Processing
    InputData = "DP_1"
    HandleMissingData = "DP_2"
    EncodeData = "DP_3"
    SplitData = "DP_4"
    FeatureScaleData = "DP_5"
    DropColumns = "DP_DC"
    TimeStepData = "DP_TSP"


    # Machine Learning
    SimpleLinearRegression = "ML_R_1"
    SimpleLinearRegressionPredict = "ML_R_1_P"
    MultipleLinearRegression = "ML_R_1"
    MultipleLinearRegressionPredict = "ML_R_1_P"
    PolynomialLinearRegression = "ML_R_1"
    PolynomialLinearRegressionPredict = "ML_R_1_P"
    SupportVectorRegression = "ML_R_1"
    SupportVectorRegressionPredict = "ML_R_1_P"
    DecisionTreeRegression = "ML_R_1"
    DecisionTreeRegressionPredict = "ML_R_1_P"
    RandomForestRegression = "ML_R_1"
    RandomForestRegressionPredict = "ML_R_1_P"


    # Deep Learning
    ArtificialNeuralNetworkInit = "DL_ANN_I"
    ArtificialNeuralNetworkTrain = "DL_ANN_T"
    ArtificialNeuralNetworkEvaluate = "DL_ANN_E"
    ArtificialNeuralNetworkPredict = "DL_ANN_P"

    SelfOrganizingMapsInit = "DL_SOM_I"
    SelfOrganizingMapsTrain = "DL_SOM_T"
    SelfOrganizingMapsPredict = "DL_SOM_P"
    
    SelfOrganizingMapsInit = "DL_SOM_I"
    SelfOrganizingMapsTrain = "DL_SOM_T"
    SelfOrganizingMapsPredict = "DL_SOM_P"
    
    RestrictedBoltzmannMachineInit = "DL_RBM_I"
    RestrictedBoltzmannMachineTrain = "DL_RBM_T"
    RestrictedBoltzmannMachineTransform = "DL_RBM_TR"