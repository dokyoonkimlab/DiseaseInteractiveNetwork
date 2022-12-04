
import pandas as pd
import numpy as np
from sklearn import metrics
import scipy.sparse

class performance_measure:
    def correlations(f, y):
        corr, p_value = stats.spearmanr(f, y)
        num = len(f)
        stderr = 1.0 / math.sqrt(num-3)
        delta = 1.96 * stderr
        lower = math.tanh(math.atanh(corr)-delta)
        upper = math.tanh(math.atanh(corr)+delta)
        return corr, p_value, lower, upper

### Load disease-snp association data ##
# N_snps = 39382
# N_diseases (phecode) = 427 ||  p-value < 1e-4, N_cases >= 1000
# dimension of disease_snp = 427 by 39382

disease_snp = scipy.sparse.load_npz("./data_bioinfo/disease_snp.npz").toarray()

snp_list = pd.read_csv("./data_bioinfo/snp_list_rsid.csv", header=None)[0]
disease_list = pd.read_csv("./data_bioinfo/phecode_list.csv", header=None)[0]
disease_info = pd.read_csv("./data_bioinfo/full_phecode_list.csv")

disease_snp = pd.DataFrame(disease_snp)
disease_snp.columns = [snp_list]
disease_snp.index = [disease_list]
########################################


### Constructign DDN with Synergistic and Antagonistic associations
W = metrics.pairwise.cosine_similarity(disease_snp)
pos_direction = np.where(W > 0) # synergsitic assocaition
neg_direction = np.where(W < 0) # antagonistic association

### Graph-based SSL with signed network
# A signed degree matrix: D
# A signed graph Laplacian matrix: L
# SSL parameter: mu
# closed form solution: f = inv(identity + mu*L) @ y

########
mu_ = 10
########

D = np.diag(np.sum(np.abs(W), 0))
L = D - W
inversed_L = np.linalg.inv(np.eye(len(W)) + mu_ * L)

### Predicting direct / inverse comorbiidty 
# f: predicted outcome for storing
# y: seed label for index disease of interest
# idx_ = index disease of interest accroding to disease_list

disease_list  = disease_list.to_numpy()


########
#idx_ = 42 # Type 2 diabetes (PheCode = 250.2)
f = np.zeros(len(W))
y = np.zeros(len(W))
y[idx_] = 1

f = inversed_L @ y
########


target_disease = disease_list[idx_]
Labeled_id = np.where(disease_info == target_disease)[0]

if (Labeled_id != idx_):
    print("index and phenotypes does not matched")

# Import pre-calculated relative risk and phi correlation for selected disease
RR_phi_location = "./data_bioinfo/EHR_comorbidity_UKBB/" + disease_list[Labeled_id] + ".pkl"
Ground_truth = pd.read_pickle(RR_phi_location[0])

f_score = pd.DataFrame(f)
f_score.columns = ['f_score']
Summary_table = pd.concat([Ground_truth["PheCode"], disease_info["description"], disease_info["category"], f_score, Ground_truth["RR"], Ground_truth["phi"], Ground_truth["pval"]], axis=1)

out_filename = "./predicted_results/"+disease_info["code2"][idx_] + ".csv"

Summary_table.to_csv(out_filename)