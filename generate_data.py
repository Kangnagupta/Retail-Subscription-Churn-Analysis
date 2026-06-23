import pandas as pd
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
random.seed(42)

# --- 1. Generate Customers ---
NUM_CUSTOMERS = 1000
cities = ['Delhi', 'Mumbai', 'Bangalore', 'Chandigarh', 'Jaipur', 'Lucknow']

customers = []
for i in range(1, NUM_CUSTOMERS + 1):
    tier = 'Premium' if random.random() < 0.3 else 'Standard' # 30% Premium
    customers.append({
        'customer_id': f'CUST_{i:04d}',
        'age': random.randint(18, 55),
        'city': random.choice(cities),
        'tier': tier,
        'join_date': datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))
    })

df_customers = pd.DataFrame(customers)

# --- 2. Generate Support Logs & Embed the "Business Insight" ---
issue_types = ['Billing Error', 'Damaged Item', 'Shipping Delay', 'Missing Item']
support_logs = []
ticket_counter = 1

for cust in customers:
    # 60% chance a customer opened a ticket
    if random.random() < 0.6:
        issue = random.choice(issue_types)
        # If it's a shipping delay, randomly assign 1 to 7 days to resolve
        days_resolved = random.randint(1, 7) if issue == 'Shipping Delay' else random.randint(1, 3)
        
        support_logs.append({
            'ticket_id': f'TKT_{ticket_counter:04d}',
            'customer_id': cust['customer_id'],
            'issue_type': issue,
            'days_to_resolve': days_resolved
        })
        ticket_counter += 1

df_support = pd.DataFrame(support_logs)

# --- 3. Generate Subscriptions (Linking Churn to Shipping Delays) ---
categories = ['Skincare', 'Makeup', 'Haircare', 'Fragrance']
subscriptions = []

for cust in customers:
    status = 'Active'
    cancel_date = None
    
    # Check if this customer had a bad shipping experience
    cust_tickets = [t for t in support_logs if t['customer_id'] == cust['customer_id']]
    bad_shipping = any(t['issue_type'] == 'Shipping Delay' and t['days_to_resolve'] > 3 for t in cust_tickets)
    
    # The Business Logic: High churn for Premium users with bad shipping
    if cust['tier'] == 'Premium' and bad_shipping:
        churn_prob = 0.45 # 45% chance to churn
    else:
        churn_prob = 0.08 # 8% normal churn baseline
        
    if random.random() < churn_prob:
        status = 'Churned'
        cancel_date = cust['join_date'] + timedelta(days=random.randint(30, 180))

    subscriptions.append({
        'sub_id': f'SUB_{cust["customer_id"].split("_")[1]}',
        'customer_id': cust['customer_id'],
        'box_category': random.choice(categories),
        'status': status,
        'cancel_date': cancel_date.strftime('%Y-%m-%d') if cancel_date else None
    })

df_subs = pd.DataFrame(subscriptions)

# --- 4. Export to CSV ---
df_customers.to_csv('customers.csv', index=False)
df_support.to_csv('support_logs.csv', index=False)
df_subs.to_csv('subscriptions.csv', index=False)

print("Success! Generated customers.csv, support_logs.csv, and subscriptions.csv in your current folder.")




import pandas as pd
from sqlalchemy import create_engine

# 1. Read the CSV files you generated and load them into Python DataFrames
df_customers = pd.read_csv('customers.csv')
df_subs = pd.read_csv('subscriptions.csv')
df_support = pd.read_csv('support_logs.csv')

# 2. Establish the connection to your new PostgreSQL database
# IMPORTANT: Change 'yourpassword' to the actual password you set for pgAdmin
engine = create_engine('postgresql://postgres:yourpassword@localhost:5432/retail_db')

# 3. Automatically create tables and upload data from Python into SQL
df_customers.to_sql('customers', engine, if_exists='replace', index=False)
df_subs.to_sql('subscriptions', engine, if_exists='replace', index=False)
df_support.to_sql('support_logs', engine, if_exists='replace', index=False)

print("Success! Data loaded from CSVs and pushed to PostgreSQL!")