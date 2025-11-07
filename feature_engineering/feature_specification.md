# 🧩 Feature Engineering Specification  
**Project:** Customer Churn Prediction  
**Author:** Gonçalo Marques 
**Last Updated:** 07/11/2025  
**Purpose:** Define engineered features and transformation logic for modeling customer churn.

---

## 1. Overview

Based on the exploratory data analysis of the IBM Telco Customer Churn dataset, several customer-related and service-related variables were identified as potential predictors of churn.  
This document describes the new **engineered features**, **data transformations**, and **hypothesized relationships** that will be implemented in the modeling pipeline.  
The goal is to enrich the dataset with more interpretable and predictive attributes while keeping the process reproducible in Databricks and Snowflake.

---

## 2. New Features

| **Feature Name** | **Type** | **Definition / Calculation** | **Business Rationale** |
|------------------|----------|------------------------------|------------------------|
| `tenure_group` | Categorical | Bucket tenure into intervals (0–12, 13–24, 25–48, 49+ months) | New customers often churn early; grouping captures non-linear risk patterns. |
| `service_count` | Numeric | Count number of “Yes” values across service columns (`OnlineSecurity`, `TechSupport`, `StreamingTV`, etc.) | Measures product adoption and engagement. |
| `avg_monthly_charge` | Numeric | `TotalCharges / tenure` | Identifies high-value or price-sensitive customers. |
| `is_auto_payment` | Binary | 1 if payment method includes “automatic” or “credit card”; 0 otherwise. | Auto-pay options reduce involuntary churn due to failed payments. |
| `contract_duration` | Categorical | Map contract type to duration (`Month-to-month` = 1, `One year` = 12, `Two year` = 24). | Longer commitments usually lower churn. |
| `paperless_flag` | Binary | 1 if `PaperlessBilling` = “Yes”; else 0. | Paperless customers may have different digital engagement. |
| `internet_type` | Categorical | Simplify `InternetService` into “DSL”, “Fiber”, or “None”. | Streamlines categorical encoding and highlights key service differences. |
| `has_tech_support` | Binary | 1 if `TechSupport` = “Yes”; else 0. | Support availability strongly correlates with retention. |
| `has_streaming` | Binary | 1 if `StreamingTV` or `StreamingMovies` = “Yes”. | Indicates content engagement; may increase loyalty. |
| `is_senior` | Binary | 1 if `SeniorCitizen` = 1; else 0. | Tests whether seniors churn at different rates. |
| `dependents_flag` | Binary | 1 if `Dependents` = “Yes”; else 0. | Customers with dependents may be more stable. |
| `monthly_charge_bucket` | Categorical | Bin `MonthlyCharges` into “Low”, “Medium”, “High”. | Captures non-linear churn patterns across price tiers. |
| `high_value_customer` | Binary | 1 if `TotalCharges` above median **and** `tenure` > 24 months. | Identifies loyal, high-spend customers for retention strategies. |

---

## 3. Transformation Rules

| **Transformation** | **Description / Purpose** | **Columns Affected** |
|---------------------|---------------------------|----------------------|
| Missing Value Handling | Replace null numeric values with median or 0; fill missing categorical with “Unknown”. | All |
| Type Conversion | Ensure numeric columns (`TotalCharges`, `tenure`, `MonthlyCharges`) are numeric. | Tenure, TotalCharges |
| Encoding | One-hot encode categorical variables such as `Contract`, `InternetService`, `PaymentMethod`. | Categorical columns |
| Normalization / Scaling | Standardize numeric variables for models sensitive to scale. | MonthlyCharges, service_count, TotalCharges |
| Binary Mapping | Convert Yes/No fields to 1/0. | All Yes/No categorical fields |
| Drop Irrelevant Columns | Remove identifiers and redundant columns. | customerID, any exact duplicates |

---

## 4. Hypothesis on Feature Importance

| **Feature** | **Expected Impact** | **Rationale** |
|--------------|--------------------|---------------|
| `tenure_group` | High | Short-tenure customers churn more frequently. |
| `contract_duration` | High | Month-to-month customers have higher churn risk. |
| `has_tech_support` | High | Tech support reduces customer frustration. |
| `service_count` | Medium | More services imply stronger commitment. |
| `avg_monthly_charge` | Medium | Very high costs may drive voluntary churn. |
| `is_auto_payment` | Medium | Auto-pay reduces involuntary churn. |
| `dependents_flag` | Low | May have small stabilizing effect. |
| `is_senior` | Low | Churn pattern might vary slightly by age group. |

---

## 5. Implementation Plan

**Environment:** Databricks (PySpark)  
**Data Source:** Cleaned dataset from AWS S3 / Azure Blob  
**Output Target:** Snowflake table `CHURN_ANALYTICS.FEATURED_CUSTOMERS`

**Workflow:**
1. Load cleaned dataset from ETL output.  
2. Apply the feature creation logic defined above in Spark.  
3. Validate new feature distributions and missing values.  
4. Save the enriched dataset to Snowflake for model training.

---

## 6. Next Steps

- [ ] Implement these transformations in Databricks.  
- [ ] Validate engineered features for accuracy and data drift.  
- [ ] Update this specification if new features are added during modeling.  
- [ ] Proceed to **Phase 3: Model Development and Evaluation**.

---

### 📎 Notes
- All transformations will be version-controlled in Git under the `data_pipeline/` and `feature_engineering/` directories.  
- Documentation and test notebooks will be maintained to ensure reproducibility across environments.

