import os
from dhanhq import dhanhq

# 1. GitHub Secrets se keys uthana
client_id = os.getenv('DHAN_CLIENT_ID')
access_token = os.getenv('DHAN_ACCESS_TOKEN')

# 2. Dhan Connection
dhan = dhanhq(client_id, access_token)

def check_connection():
    print("--- SAMRAT AI TRADER STARTING ---")
    
    # Account balance check karna
    funds = dhan.get_fund_limits()
    
    if funds['status'] == 'success':
        balance = funds['data']['availabelBalance']
        print(f"Connection Successful! ✅")
        print(f"Aapke Trading Account mein Balance: ₹{balance}")
    else:
        print("Galti: Dhan se connect nahi ho pa rahe. Keys check karein.")

if _name_ == "_main_":
    check_connection()
