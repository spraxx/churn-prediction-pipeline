## Table of Contents
- [Project Overview](#project-overview)
- [Data Understanding](#data-understanding)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Feature Engineering](#feature-engineering)
- [Modeling & Evaluation](#modeling--evaluation)
- [Results & Insights](#results--insights)

---

## 🧩 Feature Engineering  

Following the exploratory analysis, a detailed [**Feature Engineering Specification**](feature_engineering/feature_specification.md) was created to define the new variables and data transformations used in the modeling phase.  

This document outlines how raw customer attributes are enriched into meaningful predictors — such as **tenure groups**, **service counts**, **payment behavior**, and **engagement features** — that capture key churn patterns observed during EDA.  

Each feature is documented with its **definition**, **business rationale**, and **expected impact on churn**, ensuring transparency and reproducibility throughout the data pipeline.


## 🤖 Modeling & Evaluation  

This phase focuses on building and comparing predictive models to identify customers most likely to churn.  
The full **[Modeling & Evaluation Plan](modeling/modeling_plan.md)** outlines the modeling strategy, data splitting logic, performance metrics, and evaluation visuals used to assess and interpret each algorithm.  
The emphasis is on balancing predictive accuracy with interpretability, ensuring that churn drivers are actionable for business decisions.
