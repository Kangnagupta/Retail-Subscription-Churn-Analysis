# Retail Subscription Churn Analysis: The Impact of Shipping Delays

## Project Overview
This project investigates the relationship between order fulfillment speeds and customer retention within a premium subscription service. The goal of the analysis was to identify operational bottlenecks and determine if specific shipping delay thresholds directly trigger customer churn. 

By building an end-to-end data pipeline from raw generation to final visualization, I uncovered a critical business insight: shipping delays exceeding 3 days result in a nearly 10x increase in cancellation rates.

## 🛠️ Tech Stack & Tools Used
* **Data Generation & Engineering:** Python (Pandas, NumPy) via Visual Studio Code.
* **Database Management & Analysis:** PostgreSQL (pgAdmin 4).
* **Data Visualization:** Tableau Public.
* **Version Control & Documentation:** Git and GitHub.

## ⚙️ The Process: What I Did
This project demonstrates a complete Data Analytics workflow, broken down into three main phases:

### 1. Data Generation (Python)
* Wrote Python scripts utilizing Pandas and NumPy to create a realistic, synthetic dataset representing thousands of retail subscription customers.
* Engineered complex relational tables including `customers`, `subscriptions`, and `support_logs` to simulate real-world data structures.

### 2. Data Extraction & Analysis (SQL)
* Designed and executed advanced SQL queries in PostgreSQL to join the relational tables and extract actionable business metrics.
* Calculated exact churn percentages by grouping premium customers into two distinct fulfillment categories: those who experienced standard delays (3 days or under) and those who experienced severe delays (over 3 days).
* Exported the structured query results into a clean CSV format for visualization.

### 3. Data Visualization (Tableau)
* Connected the exported SQL data directly to Tableau.
* Designed an executive-level, interactive dashboard focused on clear storytelling and immediate visual impact.
* Utilized color theory (e.g., highlighting the danger zone in orange) to draw stakeholder attention to the critical failure point in the fulfillment process.

## 📊 Key Business Insights
* **The Safe Zone (Under 3 Days):** Customers who experience delivery delays of 3 days or under have a highly stable churn rate of **5.97%**. This indicates that standard, minor delays are tolerated by the customer base.
* **The Danger Zone (Over 3 Days):** Once a shipping delay crosses the 3-day mark, customer churn aggressively spikes to **57.69%**. 
* **Actionable Recommendation:** Operations and logistics teams must prioritize fulfillment speeds to ensure premium deliveries never exceed a 3-day window. Crossing this operational threshold practically guarantees a lost customer and significantly impacts recurring revenue.

## 🚀 Interactive Dashboard
👉 [Click Here to View the Live Tableau Dashboard](https://public.tableau.com/app/profile/kangna.gupta/viz/Retail_Churn_Analysis/Dashboard1)

