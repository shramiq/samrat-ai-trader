import os
from dhanhq import dhanhq

# 1. GitHub Secrets se keys uthana
cid = os.getenv('DHAN_CLIENT_ID')
tok = os.getenv('DHAN_ACCESS_TOKEN')

# 2. Dhan Connection (Bina keyword ke)
# Hum seedha (Client ID, Access Token) bhej rahe hain
try:
    dhan = dhanhq(cid, tok)
    print("Dhan Connection Object Created Successfully! ✅")
except Exception as e:
    print(f"Connection Error: {str(e)}")

def check_balance():
    print("--- SAMRAT AI TRADER ENGINE STARTING ---")
    try:
        # 3. Account balance fetch karna
        funds = dhan.get_fund_limits()
        
        if funds.get('status') == 'success':
            data = funds.get('data', {})
            # Dhan ke different versions ke liye keys check karna
            balance = data.get('availabelBalance') or data.get('availableBalance') or 0
            print(f"SUCCESS: Aapka Dhan Balance hai: ₹{balance}")
        else:
            print(f"Dhan API Error: {funds.get('remarks', 'Invalid Credentials')}")
            
    except Exception as e:
        print(f"Technical Error: {str(e)}")

# --- DHAYAN DEIN: Yahan __ (double underscore) zaroori hai ---
if _name_ == "_main_":
    check_balance()
