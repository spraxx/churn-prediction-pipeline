# Churn Prediction Pipeline (IBM Telco)

This project builds an end-to-end **churn prediction pipeline** on the IBM **Telco Customer Churn** dataset.

The main goals are to:

- Understand which factors are most associated with customer churn.  
- Build and compare several machine learning models to predict churn.  
- Show how such a model could support customer retention strategies.

---

## Table of contents

1. Problem overview  
2. Dataset  
3. Project structure  
4. Instructions: clone & run the project  
   - 4.1. Prerequisites  
   - 4.2. Clone the repository  
   - 4.3. Create and activate a virtual environment  
   - 4.4. Install dependencies  
   - 4.5. Run the code (notebooks)  
5. Feature engineering  
6. Modeling approach  
7. Possible extensions  

---

## 1. Problem overview

Telecom operators lose money when customers **churn** (cancel their service).

The main business question is:

> Can we predict which customers are at highest risk of churning, so that the company can proactively contact them with targeted retention offers?

The outputs of this project can be used to:

- Rank customers by their probability of churn.  
- Focus retention campaigns on the riskiest customers.  
- Understand which characteristics are most strongly associated with churn.

---

## 2. Dataset

The project uses the **IBM Telco Customer Churn** dataset.

Each row corresponds to one customer. Columns describe:

- **Target**
  - `Churn` – whether the customer left within the last month (`Yes` / `No`).

- **Customer services**
  - Phone, internet, streaming, security/backup, tech support, etc.  
    Examples: `PhoneService`, `InternetService`, `OnlineSecurity`, `OnlineBackup`,  
    `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`.

- **Account information**
  - `tenure` (months with the company)  
  - contract type (month-to-month / one-year / two-year)  
  - payment method  
  - whether billing is paperless  
  - `MonthlyCharges` and `TotalCharges`

- **Demographics**
  - `gender`, `SeniorCitizen`, `Partner`, `Dependents`

The CSV is expected at:

```text
data/raw/Telco-Customer-Churn.csv
```

If the file is not present, download the IBM Telco Customer Churn dataset  
(for example from Kaggle) and save it under that path with the same filename.

---

## 3. Project structure

This repo follows a simplified “cookiecutter data science” layout:

```text
.
├── data
│   ├── raw/          # original CSV (Telco-Customer-Churn.csv)
│   ├── interim/      # intermediate data
│   └── processed/    # cleaned / feature-engineered data (optional)
├── notebooks
│   ├── 01_eda_intro.ipynb       # exploratory data analysis
│   └── 02_model_training.ipynb  # model training and evaluation
├── src
│   ├── data
│   │   └── make_dataset.py      # data loading + basic cleaning
│   ├── features
│   │   └── build_features.py    # feature engineering
│   └── models                   # (optional) standalone training scripts
├── models/                      # trained models can be saved here
├── reports/                     # figures / reports (optional)
├── requirements.txt
├── setup.py                     # so `src` can be installed as a package
└── README.md
```

The notebooks import functions from `src`, so that data loading and feature
engineering are reusable and not duplicated.

---

## 4. Instructions: clone & run the project

This section is for anyone who wants to run the project on their own machine.

### 4.1. Prerequisites

You will need:

- Python **3.10+**  
- `git`  
- `pip`  
- (Optional) `conda` or `venv` for virtual environments  
- (Optional) Jupyter Lab or the classic Jupyter Notebook  

### 4.2. Clone the repository

If the project is hosted on GitHub:

```bash
git clone <YOUR-REPO-URL>.git
cd churn-prediction-pipeline
```

If you downloaded a ZIP instead, unzip it and `cd` into the project folder.

### 4.3. Create and activate a virtual environment

Using `venv`:

```bash
python -m venv .venv

# On macOS / Linux:
source .venv/bin/activate

# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
```

You should now see `(.venv)` at the beginning of your terminal prompt.

### 4.4. Install dependencies

Install the Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

The modeling notebook also uses **PyTorch**.  
If it is not already installed, add:

```bash
pip install torch
```

> For GPU / specific OS instructions, refer to the official PyTorch docs.

Finally, install the local `src` package in editable mode, so imports like  
`from src.data.make_dataset import load_and_clean_churn_data` work:

```bash
pip install -e .
```

### 4.5. Run the code (notebooks)

From the project root:

```bash
jupyter notebook
```

(or `jupyter lab` if you prefer that)

Then open and run the notebooks in order:

1. **`notebooks/01_eda_intro.ipynb`**

   - Loads and cleans the raw dataset.  
   - Explores churn rates by contract, payment method, tenure, etc.  
   - Builds intuition on which variables matter.

2. **`notebooks/02_model_training.ipynb`**

   - Reuses the same data cleaning & feature engineering functions.  
   - Builds preprocessing + modeling pipelines.  
   - Trains and tunes several models.  
   - Compares their performance and adjusts the decision threshold.

Make sure the Jupyter kernel you select is the one from your virtual environment.

---

## 5. Feature engineering

Feature engineering is implemented in:

```text
src/features/build_features.py
```

The main function is:

```python
from src.features.build_features import add_churn_features
```

It creates the following additional features on top of the original columns:

1. **Number of services (`num_services`)**  
   Based on:

   `PhoneService`, `MultipleLines`, `InternetService`,  
   `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`,  
   `TechSupport`, `StreamingTV`, `StreamingMovies`.

   For each customer, it counts how many of these are `"Yes"`.  

   **Intuition:** customers using more services are more “locked in” and may churn
   differently from those using only one.

2. **Tenure bucket (`tenure_bucket`)**  
   Based on `tenure` (months), the code groups it into categories such as:

   - `0–1y`, `1–2y`, `2–4y`, `4–6y`, `6y+`.

   **Intuition:** churn risk is usually higher early in the relationship and lower for
   long-tenure customers. The bucketed version is more interpretable and easier for
   some models to use than a raw continuous value.

3. **Average lifetime spend (`charges_per_month_lifetime`)**  
   Based on `TotalCharges` and `tenure`:

   \[
   	ext{charges\_per\_month\_lifetime} =
   rac{	ext{TotalCharges}}{\max(	ext{tenure}, 1)}
   \]

   (we replace tenure 0 with 1 to avoid division by zero).  

   **Intuition:** this approximates **average monthly spend over the entire relationship**,  
   which can capture value segments beyond the current `MonthlyCharges` alone.

4. **Binary flags for important patterns**

   - `has_fiber_optic` – 1 if `InternetService == "Fiber optic"`, else 0.  
   - `is_electronic_check` – 1 if `PaymentMethod == "Electronic check"`, else 0.  
   - `is_paperless` – 1 if `PaperlessBilling` == "Yes", else 0.

   **Intuition:** these flags isolate specific behaviours that (based on EDA on this
   dataset) are often strongly associated with higher or lower churn  
   (e.g. electronic check users tend to churn more).

The function checks that required columns are present before creating each feature,
so it will not crash if some columns are missing.

---

## 6. Modeling approach

The main modeling workflow (implemented in `notebooks/02_model_training.ipynb`) is:

1. **Load and clean the data**

   - Use `load_and_clean_churn_data` from `src.data.make_dataset` to:
     - Convert `TotalCharges` to numeric and drop invalid rows.  
     - Drop entries with `tenure == 0`.  
     - Encode `Churn` as 0/1.

2. **Apply feature engineering**

   - Use `add_churn_features` from `src.features.build_features` to add the features
     described above.

3. **Train / test split**

   - Perform a stratified train/test split to preserve the churn proportion.

4. **Preprocessing pipeline**

   - Build a `ColumnTransformer` that:
     - scales numeric features with `StandardScaler`,  
     - one-hot encodes categorical features with `OneHotEncoder`.  
   - Wrap the preprocessor and model into a single `Pipeline` so that all steps are
     applied consistently during training and evaluation.

5. **Models trained (with hyperparameter search)**

   - **Logistic Regression** – interpretable baseline; tuned with `RandomizedSearchCV`.  
   - **Random Forest** – tree ensemble that can capture non-linear interactions.  
   - **HistGradientBoostingClassifier** – gradient boosting for tabular data.  
   - **PyTorch MLP** – a small neural network trained on the preprocessed features.

6. **Evaluation and threshold tuning**

   - Compare models using:
     - ROC-AUC,  
     - accuracy, precision, recall, F1.  
   - Perform **threshold tuning** for the best model:
     - By default, probability ≥ 0.5 → churn.  
     - Here, different thresholds are explored to trade off recall vs precision,
       depending on how expensive false negatives / false positives are for the
       business.

---

## 7. Possible extensions

Some ideas for future work:

- Save the best model to the `models/` folder (e.g. using `joblib` or `pickle`).  
- Add unit tests for:
  - `load_and_clean_churn_data`  
  - `add_churn_features`  
- Move PyTorch training logic from the notebook into `src/models/` as a script.  
- Build a simple API or web UI that scores new customers using the trained model.  
- Add cost-based evaluation (e.g. expected savings from a retention campaign).  
