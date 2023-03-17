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
    MultipleLinearRegression = "ML_R_2"
    MultipleLinearRegressionPredict = "ML_R_2_P"
    PolynomialLinearRegression = "ML_R_3"
    PolynomialLinearRegressionPredict = "ML_R_3_P"
    SupportVectorRegression = "ML_R_4"
    SupportVectorRegressionPredict = "ML_R_4_P"
    DecisionTreeRegression = "ML_R_5"
    DecisionTreeRegressionPredict = "ML_R_5_P"
    RandomForestRegression = "ML_R_6"
    RandomForestRegressionPredict = "ML_R_6_P"
    LogisticRegression = "ML_CN_1"
    LogisticRegressionPredict = "ML_CN_1_P"
    KNearestNeighbors = "ML_CN_2"
    KNearestNeighborsPredict = "ML_CN_2_P"
    SupportVectorMachine = "ML_CN_3"
    SupportVectorMachinePredict = "ML_CN_3_P"
    KernelSupportVectorMachine = "ML_CN_4"
    KernelSupportVectorMachinePredict = "ML_CN_4_P"
    NaiveBayes = "ML_CN_5"
    NaiveBayesPredict = "ML_CN_5_P"
    DecisionTreeClassification = "ML_CN_6"
    DecisionTreeClassificationPredict = "ML_CN_6_P"
    RandomForestClassification = "ML_CN_7"
    RandomForestClassificationPredict = "ML_CN_7_P"
    HierarchicalClustering = "ML_CG_5"
    HierarchicalClusteringPredict = "ML_CG_5_P"
    XGBoost = "MS_XGBOOST"
    XGBoostPredict = "MS_XGBOOST_P"
    
    # Auto Machine Learning
    AutoRegression = "AUTO_R_1"
    AutoClassification = "AUTO_CN_1"

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
