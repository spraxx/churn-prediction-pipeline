# 🤖 Modeling & Evaluation Plan  

**Project:** Customer Churn Prediction  
**Author:** [Your Name]  
**Last Updated:** [Insert Date]  
**Purpose:** Define modeling strategy, evaluation metrics, and validation process for predicting customer churn.

---

## 1. Objective  

The goal of this phase is to build predictive models that estimate the likelihood of a customer churning based on demographic, account, and service-related features.  
The models will be compared using consistent evaluation metrics, with a focus on **explainability**, **performance**, and **business interpretability**.

---

## 2. Modeling Approach  

The modeling will follow a structured pipeline:  

1. **Data Load & Preparation**
   - Import feature-engineered dataset from Snowflake.  
   - Split into training (80%) and testing (20%) datasets.  
   - Apply scaling and encoding transformations as defined in the Feature Engineering Specification.

2. **Model Selection**
   A diverse set of algorithms will be tested to capture both linear and non-linear relationships:
   - **Logistic Regression** — baseline interpretable model for binary classification.  
   - **Random Forest Classifier** — non-linear ensemble model that handles mixed data types and feature interactions.  
   - **XGBoost / LightGBM** — gradient boosting models for optimal predictive accuracy.  
   - **Neural Network (TensorFlow / PyTorch)** — test performance of deep learning model for pattern recognition.  

   Each model will be trained, tuned, and compared using the same dataset split and evaluation framework.

3. **Feature Importance & Explainability**
   - Use feature importance plots (for tree-based models).  
   - Apply SHAP values or permutation importance for model interpretability.  
   - Highlight top churn drivers for business decision-making.

---

## 3. Data Splitting Strategy  

| **Dataset** | **Proportion** | **Purpose** |
|--------------|----------------|--------------|
| Training | 80% | Used to train and tune model parameters |
| Testing | 20% | Used for final evaluation of model performance |

Additionally, **Stratified Splitting** will be applied to preserve the churn vs. non-churn ratio in both sets.  

If necessary, **class imbalance techniques** such as SMOTE, undersampling, or class weighting will be tested.

---

## 4. Evaluation Metrics  

Since this is a **binary classification** problem with **class imbalance**, accuracy alone is not sufficient.  
The following metrics will be used for a balanced view of model performance:

| **Metric** | **Purpose** |
|-------------|-------------|
| **ROC-AUC** | Measures overall discriminative power of the model. |
| **Precision** | How many predicted churns are actual churns (minimize false positives). |
| **Recall** | How many actual churns the model correctly identifies (minimize false negatives). |
| **F1-score** | Harmonic mean of precision and recall; balances both metrics. |
| **Confusion Matrix** | Visualizes misclassification patterns. |

Threshold tuning will be performed to balance business trade-offs (e.g., maximizing recall for retention targeting).

---

## 5. Model Validation  

Each model will undergo **cross-validation** (5-fold) to assess stability and reduce overfitting risk.  
Metrics will be averaged across folds, and variance will be analyzed to evaluate model robustness.

---

## 6. Model Tuning  

For each algorithm, hyperparameter optimization will be performed using:
- **Grid Search** or **Random Search** in scikit-learn.  
- Evaluation based on ROC-AUC and F1-score from cross-validation.  

Example tuning parameters (to be implemented later):
- Logistic Regression: `C`, regularization type  
- Random Forest: `n_estimators`, `max_depth`, `min_samples_split`  
- XGBoost: `learning_rate`, `max_depth`, `n_estimators`, `subsample`

---

## 7. Model Comparison & Selection  

After tuning, the models will be compared on the **test dataset** using the chosen metrics.  
A summary table will record all results for transparency.

| **Model** | **ROC-AUC** | **Precision** | **Recall** | **F1-score** | **Interpretability** | **Selected?** |
|------------|--------------|---------------|-------------|---------------|---------------------|---------------|
| Logistic Regression |  |  |  |  | High | ✅ Baseline |
| Random Forest |  |  |  |  | Medium |  |
| XGBoost |  |  |  |  | Medium |  |
| Neural Network |  |  |  |  | Low |  |

The final model will be selected based on both **predictive power** and **explainability**, depending on the project goal (accuracy vs. interpretability).

---

## 8. Visualization Plan  

The following plots will be created to interpret and communicate model performance:
- ROC Curve  
- Precision-Recall Curve  
- Confusion Matrix  
- Feature Importance Plot  
- SHAP Summary Plot  

These visuals will be saved in the `visualizations/model_evaluation/` folder and referenced in the README.

---

## 9. Deliverables  

| **Deliverable** | **Description** |
|------------------|----------------|
| `modeling_plan.md` | This document describing modeling approach and evaluation strategy. |
| Trained models (`.pkl` or `.sav`) | Saved serialized model files for reuse. |
| Evaluation visuals | Stored in `visualizations/model_evaluation/`. |
| Model performance summary | Markdown or notebook with all metric results. |

---

## 10. Next Steps  

- [ ] Implement model training and tuning in Databricks or local Python.  
- [ ] Evaluate and compare models on test data.  
- [ ] Interpret top predictors using feature importance / SHAP.  
- [ ] Document results in **Results & Insights** section.  
- [ ] Save final model artifact and metrics for deployment.

---

### 📎 Notes
- Model reproducibility will be ensured by fixing random seeds.  
- All experiments and parameters will be version-controlled via Git.  
- If model results are exported to Snowflake, metadata will be logged for traceability.

