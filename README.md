# DiseaseInteractiveNetwork

## Discovering comorbid diseases using an inter-disease interactivity network based on biobank-scale PheWAS data

### Requirements
This implementation is conducted by the following packages (to be installed independently)
  * pandas
  * numpy
  * sklearn
  * scipy

### Data Description
1. Used/Converted datasets of constructing DDN
  * UK Biobank PheWAS summary statistics were obtained from https://www.leelabsg.org/resources
```  
./data_bioinfo/disease_snp.npz  # 427 diseases by 39382 SNPs
./data_bioinfo/full_phecode_list.csv # description of 427 diseases with PheCode
./data_bioinfo/snp_list_rsid.csv # list of used SNPs in this analysis
```

2. Generated results with proposed method
```
./data_bioinfo/predicted_results_for_427_diseases.zip # Predicted scores from graph-based SSL, Relative risk & Phi-correlations obtained from EHR data
```
Similar implementation of graph-based SSL can be found at scikit-learn (sklearn.semi_supervised.LabelPropagation) <br>
This file explains step by step how to use graph-based SSL.
```
Toy_Example_graph_based_SSL.ipynb # Instructions
```
  
  Functional version and toy example demonstration
```  
SSL.py # Function for graph-based SSL
test_main.py # Toy example
```
  
### Note
  1. Implementation of variable selection also can be found at scikit-learn <br>
    a. from sklearn.linear_model import LogisticRegression<br>
    b. from sklearn.ensemble import ExtraTreesClassifier<br>
    c. from sklearn.svm import SVC<br>
    d. from sklearn.feature_selection import RFE<br>
  <br>
  2. To protect patient's private information, we can not share the data. (To reqeust data access, please contact authors: Seung Mi Lee. M.D., Ph.D.)
