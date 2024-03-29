class function_codes:
    # Data Processing
    DataInput = "DP_1"
    HandleMissingData = "DP_2"
    DataEncoding = "DP_3"
    DataSplitting = "DP_4"
    FeatureScaleData = "DP_5"
    DropColumns = "DP_6"  # "DP_DC"
    TimeStepData = "DP_7"  # "DP_TSP"

    AutomatedDataProcessing = "DP_ADP"
    FeatureSampling = "DP_FSP"
    ParseDatetime = "DP_PDT"
    ReorderColumn = "DP_ROC"
    ReshapeArray = "DP_RSH"
    ColumnAstype = "DP_ASP"
    ShowDuplicates = "DP_SDC"
    DropDuplicates = "DP_DRD"
    ScalarToNdarray = "DP_STN"
    ImageToNdarray = "DP_ITN"
    DatasetInfo = "DP_INF"
    DatasetCorrelations = "DP_CRR"
    DatasetDescription = "DP_DSC"
    DatasetUniques = "DP_UNQ"
    StatsCounts = "DP_STC"
    PrincipalComponentAnalysis = "DP_PCA"
    TextVectorizer = "DP_VEC"
    Resampler = "DP_RES"

    # Data Visualization
    ScatterPlot = "DP_SCP"
    OrdinaryPlot = "DP_ORD"
    CompareScatterPlots = "DP_CSP"
    PiePlot = "DP_PIE"
    HeatmapPlot = "DP_HMP"

    # Machine Learning
    SimpleLinearRegression = "ML_R_1"
    SimpleLinearRegressionPredict = "ML_R_1_P"
    SimpleLinearRegressionPredict = "ML_R_1_M"
    MultipleLinearRegression = "ML_R_2"
    MultipleLinearRegressionPredict = "ML_R_2_P"
    MultipleLinearRegressionPredict = "ML_R_2_M"
    PolynomialLinearRegression = "ML_R_3"
    PolynomialLinearRegressionPredict = "ML_R_3_P"
    PolynomialLinearRegressionPredict = "ML_R_3_M"
    SupportVectorRegression = "ML_R_4"
    SupportVectorRegressionPredict = "ML_R_4_P"
    SupportVectorRegressionPredict = "ML_R_4_M"
    DecisionTreeRegression = "ML_R_5"
    DecisionTreeRegressionPredict = "ML_R_5_P"
    DecisionTreeRegressionPredict = "ML_R_5_M"
    RandomForestRegression = "ML_R_6"
    RandomForestRegressionPredict = "ML_R_6_P"
    RandomForestRegressionPredict = "ML_R_6_M"
    LogisticRegression = "ML_CN_1"
    LogisticRegressionPredict = "ML_CN_1_P"
    LogisticRegressionPredict = "ML_CN_1_M"
    KNearestNeighbors = "ML_CN_2"
    KNearestNeighborsPredict = "ML_CN_2_P"
    KNearestNeighborsPredict = "ML_CN_2_M"
    SupportVectorMachine = "ML_CN_3"
    SupportVectorMachinePredict = "ML_CN_3_P"
    SupportVectorMachinePredict = "ML_CN_3_M"
    KernelSupportVectorMachine = "ML_CN_4"
    KernelSupportVectorMachinePredict = "ML_CN_4_P"
    KernelSupportVectorMachinePredict = "ML_CN_4_M"
    NaiveBayes = "ML_CN_5"
    NaiveBayesPredict = "ML_CN_5_P"
    NaiveBayesPredict = "ML_CN_5_M"
    DecisionTreeClassification = "ML_CN_6"
    DecisionTreeClassificationPredict = "ML_CN_6_P"
    DecisionTreeClassificationPredict = "ML_CN_6_M"
    RandomForestClassification = "ML_CN_7"
    RandomForestClassificationPredict = "ML_CN_7_P"
    RandomForestClassificationPredict = "ML_CN_7_M"
    HierarchicalClustering = "ML_CG_1"
    HierarchicalClusteringPredict = "ML_CG_1_P"
    HierarchicalClusteringPredict = "ML_CG_1_M"
    KMeansClustering = "ML_CG_2"
    KMeansClusteringPredict = "ML_CG_2_P"
    KMeansClusteringPredict = "ML_CG_2_M"
    XGBoost = "MS_XGBOOST"
    XGBoostPredict = "MS_XGBOOST_P"
    GridSearch = "ML_GRID"
    SHAPExplain = "ML_SHAP"
    IsolationForest = "ML_ISF"
    IsolationForestPredict = "ML_ISF_P"
    IsolationForestMetrics = "ML_ISF_M"

    # Auto Machine Learning
    AutoRegression = "AUTO_R_1"
    AutoRegressionPredict = "AUTO_R_1_P"
    AutoRegressionMetrics = "AUTO_R_1_M"
    AutoClassification = "AUTO_CN_1"
    AutoClassificationPredict = "AUTO_CN_1_P"
    AutoClassificationMetrics = "AUTO_CN_1_M"

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

    AutoDeepLearningPredict = "A_DL_ALL_P"
    AutoDeepLearningEvaluate = "A_DL_ALL_E"
