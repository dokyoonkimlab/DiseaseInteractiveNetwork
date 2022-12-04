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

2. Generated results with proposed method: Predicted scores from graph-based SSL, Relative risk & Phi-correlations obtained from EHR data
```
./data_bioinfo/predicted_results_for_427_diseases.zip 
```

3. Generated Relative risk & Phi-correlations for 427 diseases
```
./data_bioinfo/EHR_comorbidity_UKBB/ **.pkl 
```
### Implemenations of comorbidity scoring
* The following codes expalains simple examples for predicting direct/inverse comorbidity
* Hyperparameters
  ** idx_ : index disease of interest (index according to full_phecode_list.csv
```
main.py 
```
