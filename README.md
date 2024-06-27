# may24-T10

## AI300 Capstone  May 2024 Saturday cohort Team 10

Team Members:
- Ardi Wira Sudarmo
- Lim Suongwei Jerry

## Deployed Flask URL:
[http://ec2-13-250-95-254.ap-southeast-1.compute.amazonaws.com/](http://ec2-13-250-95-254.ap-southeast-1.compute.amazonaws.com/)


## Final Model

### Final Model Path

`model/catboost_model_small.pkl`

### Catboost Model Parameter

Parameters are tuned using **BayesSearchCV** :
- learning_rate = 0.092
- depth=5
- iterations = 131
- random_state = 5

### Features:

The following features are selected based on highest SHAP scores

- `contract_type`
- `referrals_category` (derived from `num_referrals`)
- `tenure_months`
- `has_dependents` (derived from `num_dependants`)
- `internet_type`
- `total_monthly_fee`
- `payment_method`
- `married`
- `senior_citizen`
- `city`
- `total_charges_quarter`

### Offline AUC

Offline ROC AUC measured using k-stratified-fold validation with k=3 is *0.9107*

### Notebook path

`notebooks/Capstone_research_final.ipynb`
