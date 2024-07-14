import sqlite3
import random
from datetime import datetime
import matplotlib.pyplot as plt

# Function to generate random lead data
def generate_lead():
    lead_id = random.randint(1, 1000)
    lead_name = f"Lead{lead_id}"
    lead_status = random.choice(['handled', 'unhandled'])
    lead_created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return (lead_id, lead_name, lead_status, lead_created_at)

# Function to insert lead data into SQLite3 database
def insert_lead_into_db(lead_data):
    conn = sqlite3.connect('crm_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY,
            name TEXT,
            status TEXT,
            created_at TEXT
        )
    ''')
    cursor.execute('INSERT INTO leads (id, name, status, created_at) VALUES (?, ?, ?, ?)', lead_data)
    conn.commit()
    conn.close()

# Generating and inserting random leads into database
for _ in range(10):  # Generate 10 random leads for demonstration
    lead_data = generate_lead()
    insert_lead_into_db(lead_data)
    print(f"Inserted lead: {lead_data}")

print("Random leads generated and inserted into the database.")

# Function to query handled and unhandled leads
def query_leads(status):
    conn = sqlite3.connect('crm_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM leads WHERE status = ?', (status,))
    leads = cursor.fetchall()
    conn.close()
    return leads

# Function to update lead status
def update_lead_status(lead_id, new_status):
    conn = sqlite3.connect('crm_database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE leads SET status = ? WHERE id = ?', (new_status, lead_id))
    conn.commit()
    conn.close()
    print(f"Lead {lead_id} updated with status: {new_status}")

# Example usage:
# Query unhandled leads
unhandled_leads = query_leads('unhandled')
print("Unhandled leads:", unhandled_leads)

# Update the status of a lead
if unhandled_leads:
    first_unhandled_lead_id = unhandled_leads[0][0]
    update_lead_status(first_unhandled_lead_id, 'handled')

# Function to generate a pie chart for lead analysis
def generate_pie_chart():
    labels = ['Handled', 'Unhandled']
    sizes = [len(query_leads('handled')), len(query_leads('unhandled'))]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Distribution of Handled and Unhandled Leads')
    plt.show()

# Example usage:
generate_pie_chart()

# Function to calculate payout based on handled leads
def calculate_payout(rate_per_conversion):
    handled_leads = query_leads('handled')
    total_payout = len(handled_leads) * rate_per_conversion
    return total_payout

# Example usage:
rate_per_conversion = 50  # Define your rate per conversion
payout = calculate_payout(rate_per_conversion)
print(f"Total payout: ${payout}")


