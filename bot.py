import os
from dhanhq import dhanhq

# 1. GitHub Secrets se keys uthana
client_id = os.getenv('DHAN_CLIENT_ID')
access_token = os.getenv('DHAN_ACCESS_TOKEN')

# 2. Dhan Connection (Final Fix)
# Error ke mutabiq library sirf 1 argument (access_token) mang rahi hai
dhan = dhanhq(access_token)

def check_connection():
    print("--- SAMRAT AI TRADER ENGINE START ---")
    print(f"Checking account for Client ID: {client_id}")
    
    try:
        # 3. Account balance check karna
        # Yahan hum client_id ko function ke andar bhej rahe hain agar zaroorat padi toh
        funds = dhan.get_fund_limits()
        
        if funds.get('status') == 'success':
            data = funds.get('data', {})
            # Alag-alag version mein balance ka naam alag ho sakta hai
            balance = data.get('availabelBalance') or data.get('availableBalance') or data.get('sodLimit', 0)
            
            print(f"Connection Successful! ✅")
            print(f"Aapke Dhan Account mein Balance: ₹{balance}")
        else:
            print("Galti: Dhan se connect nahi ho pa rahe.")
            print("Dhan Message:", funds.get('remarks', 'Invalid Token'))
            
    except Exception as e:
        print(f"Technical Error: {str(e)}")
        print("Tip: Dhan Portal par jaakar naya Access Token generate karke GitHub Secrets mein update karein.")

if _name_ == "_main_":
    check_connection()
