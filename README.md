# Telco Customer Churn – EDA, Visualization & Deep Learning

Case study for **U21ADP05 – Exploratory Data Analysis and Visualization (Assignment II)**, KPR Institute of Engineering and Technology.

**Problem:** Which telecom customers are likely to churn, and why? We explore the data, test the drivers statistically, and train a PyTorch MLP to predict churn.

## Dataset
IBM Telco Customer Churn – 7,043 customers, 20 features + target `Churn` (26.5% churn).
Included at `data/Telco-Customer-Churn.csv` (source: https://github.com/IBM/telco-customer-churn-on-icp4d).

## Repository structure
```
data/        Telco-Customer-Churn.csv
src/         churn_eda_model.py (full pipeline), make_notebook.py, build_report.py
notebooks/   churn_eda_model.ipynb
figures/     15 PNG charts + 2 interactive Plotly HTML charts
report/      Project_Report.docx / Project_Report.pdf
results.json all numbers used in the report
```

## What is covered
- Cleaning: missing `TotalCharges`, duplicates, IQR outliers, feature engineering, one-hot encoding, scaling, stratified 70/15/15 split
- 9 visualizations (histograms/KDE, boxplots, segment bars, correlation heatmap, scatter, pairplot, distribution fits & Q-Q, tenure/services) + interactive Plotly charts – all 7 visualization stages
- Statistics: skewness/kurtosis, KS distribution fits, Mann-Whitney U, chi-square, Cramér's V
- Model: MLP (PyTorch), grid-search tuning, compared with Logistic Regression and Random Forest
- Evaluation: loss/accuracy curves, confusion matrix, ROC-AUC, PR curve, probability histogram, permutation importance

## Key results
| Model | Accuracy | Recall | F1 | ROC-AUC |
|---|---|---|---|---|
| MLP | 0.747 | 0.787 | 0.623 | 0.845 |
| Logistic Regression | 0.747 | 0.779 | 0.621 | 0.845 |
| Random Forest | 0.760 | 0.787 | 0.635 | 0.840 |

Churn is highest for short-tenure, month-to-month, fibre-optic, electronic-check customers without security/support add-ons.

## Run it
```bash
pip install -r requirements.txt
python src/churn_eda_model.py        # regenerates figures/ and results.json (~1 min, CPU)
python src/build_report.py           # rebuilds report/Project_Report.docx
```
