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
    ArtificialNeuralNetworkInit = "DL_ANN_S_I"
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
    
    # Auto Deep Learnning
    AutoImageClassifierInit = "A_DL_IMC_I"
    AutoImageClassifierTrain = "A_DL_IMC_T"
    
    AutoImageRegressionInit = "A_DL_IMR_I"
    AutoImageRegressionTrain = "A_DL_IMR_T"
    
    AutoTextClassifierInit = "A_DL_TXC_I"
    AutoTextClassifierTrain = "A_DL_TXC_T"
    
    AutoTextRegressionInit = "A_DL_TXR_I"
    AutoTextRegressionTrain = "A_DL_TXR_T"
    
    AutoStructuredDataClassifierInit = "A_DL_SDC_I"
    AutoStructuredDataClassifierTrain = "A_DL_SDC_T"
    
    AutoStructuredDataRegressionInit = "A_DL_SDR_I"
    AutoStructuredDataRegressionTrain = "A_DL_SDR_T"