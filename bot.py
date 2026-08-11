import os
from dhanhq import dhanhq

# 1. GitHub Secrets se keys uthana
client_id = os.getenv('DHAN_CLIENT_ID')
access_token = os.getenv('DHAN_ACCESS_TOKEN')

def run_bot():
    print("--- SAMRAT AI TRADER ENGINE STARTING ---")
    try:
        # 2. Dhan Connection (Dhyan se dekhna)
        # Hum bina keyword ke bhej rahe hain: Client ID aur Access Token
        dhan = dhanhq(client_id, access_token)
        print("Dhan Connection Object Created! ✅")
        
        # 3. Account balance check karna
        funds = dhan.get_fund_limits()
        
        if funds.get('status') == 'success':
            data = funds.get('data', {})
            # Dhan ke different versions ke liye keys check karna
            balance = data.get('availabelBalance') or data.get('availableBalance') or 0
            print(f"SUCCESS: Aapka Dhan Balance hai: ₹{balance}")
        else:
            print(f"Dhan API Error: {funds.get('remarks', 'Invalid Credentials')}")
            
    except Exception as e:
        print(f"Galti: {str(e)}")

# --- DHAYAN DEIN: Yahan do-do (__) dash lagaye hain maine ---
if _name_ == "_main_":
    run_bot()
