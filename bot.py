import os
from dhanhq import dhanhq

# 1. GitHub Secrets se keys uthana
client_id = os.getenv('DHAN_CLIENT_ID')
access_token = os.getenv('DHAN_ACCESS_TOKEN')

# 2. Dhan Connection (Sahi Tarika)
# Library ko keyword ke saath bata rahe hain taaki positional error na aaye
try:
    dhan = dhanhq(client_id=client_id, access_token=access_token)
    print("Dhan Connection Object Created! ✅")
except Exception as e:
    print(f"Initial Connection Error: {str(e)}")

def check_balance():
    print("--- SAMRAT AI TRADER ENGINE START ---")
    try:
        # Account balance fetch karna
        funds = dhan.get_fund_limits()
        
        if funds.get('status') == 'success':
            data = funds.get('data', {})
            # Dhan ke alag-alag version ke liye keys
            balance = data.get('availabelBalance') or data.get('availableBalance') or 0
            print(f"SUCCESS: Aapka Dhan Balance hai: ₹{balance}")
        else:
            print(f"API Error: {funds.get('remarks', 'Invalid Token')}")
            
    except Exception as e:
        print(f"Technical Error: {str(e)}")

# --- DHAYAN DEIN: Yahan double underscore (__) zaroori hai ---
if _name_ == "_main_":
    check_balance()
