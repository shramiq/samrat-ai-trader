import os
from dhanhq import dhanhq

# 1. GitHub Secrets se keys uthana
client_id = os.getenv('DHAN_CLIENT_ID')
access_token = os.getenv('DHAN_ACCESS_TOKEN')

# 2. Dhan Connection (Final Master Fix)
# Dhan library ko teeno cheezein chahiye: Client ID, Access Token aur Account Type
# Hum yahan 'money' use kar rahe hain jo live account ke liye hota hai
try:
    dhan = dhanhq(client_id, access_token, "money")
    print("Dhan Object Created Successfully!")
except Exception as e:
    print(f"Connection Initialization Error: {str(e)}")

def check_connection():
    print("--- SAMRAT AI TRADER ENGINE START ---")
    print(f"Checking account for Client ID: {client_id}")
    
    try:
        # 3. Account balance check karna
        funds = dhan.get_fund_limits()
        
        if funds.get('status') == 'success':
            data = funds.get('data', {})
            # Dhan ke alag-alag versions ke balance keys
            balance = data.get('availabelBalance') or data.get('availableBalance') or data.get('sodLimit', 0)
            
            print(f"Connection Successful! ✅")
            print(f"Aapke Dhan Account mein Balance: ₹{balance}")
        else:
            print("Galti: Dhan API ne reject kar diya.")
            print("Message:", funds.get('remarks', 'Invalid Credentials'))
            
    except Exception as e:
        print(f"Technical Error while fetching balance: {str(e)}")
        print("Tip: Check karein ki GitHub Secrets mein Client ID aur Access Token sahi hain.")

if _name_ == "_main_":
    check_connection()
