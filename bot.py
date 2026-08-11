import os
from dhanhq import dhanhq

# 1. GitHub Secrets se keys uthana
client_id = os.getenv('DHAN_CLIENT_ID')
access_token = os.getenv('DHAN_ACCESS_TOKEN')

# 2. Dhan Connection (Fixed Version)
# Yahan humne 'client_id=' aur 'access_token=' likh diya hai taaki error na aaye
dhan = dhanhq(client_id=client_id, access_token=access_token)

def check_connection():
    print("--- SAMRAT AI TRADER ENGINE START ---")
    
    try:
        # Account balance check karna
        funds = dhan.get_fund_limits()
        
        if funds.get('status') == 'success':
            # Dhan ka data nikalne ka sahi tareeka
            data = funds.get('data', {})
            balance = data.get('availabelBalance', 'N/A')
            print(f"Connection Successful! ✅")
            print(f"Aapke Dhan Account mein Balance: ₹{balance}")
        else:
            print("Galti: Dhan se response toh mila par success nahi hua.")
            print("Message:", funds.get('remarks', 'Check API Keys'))
            
    except Exception as e:
        print(f"Technical Error: {str(e)}")
        print("Tip: Dhan Portal par jaakar dekho ki Access Token expired toh nahi ho gaya.")

if _name_ == "_main_":
    check_connection()
