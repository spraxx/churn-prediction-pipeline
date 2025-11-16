### Feature engineering

On top of the original IBM Telco columns, we create a few extra features to help the models:

1. **Number of services (`num_services`)**  
   Counts how many services a customer has (phone, internet, streaming, security, etc.).  
   Intuition: customers with more services are more “locked in” and may churn differently.

2. **Tenure bucket (`tenure_bucket`)**  
   Converts the numeric `tenure` (months) into categories:  
   `0–1y`, `1–2y`, `2–4y`, `4–6y`, `6y+`.  
   Intuition: churn risk is typically higher in the first months/years of the relationship.

3. **Average lifetime spend (`charges_per_month_lifetime`)**  
   Approximate average monthly spend:  

   \[
   \text{charges\_per\_month\_lifetime} = \frac{\text{TotalCharges}}{\text{tenure}}
   \]

   (with tenure 0 replaced by 1 to avoid division by zero).  
   Intuition: customers with different tenures but similar total spend are not equivalent; this normalizes for time.

4. **Binary flags for important patterns**  
   - `has_fiber_optic` – 1 if `InternetService == "Fiber optic"`.  
   - `is_electronic_check` – 1 if `PaymentMethod == "Electronic check"`.  
   - `is_paperless` – 1 if `PaperlessBilling == "Yes"`.

   These flags capture patterns often seen in the dataset: for example, fiber optic and electronic check customers tend to have different churn rates.
