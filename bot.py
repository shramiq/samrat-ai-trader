import os
from dhanhq import dhanhq

# 1. GitHub Secrets se keys uthana
client_id = os.getenv('DHAN_CLIENT_ID')
access_token = os.getenv('DHAN_ACCESS_TOKEN')

# 2. Dhan Connection (Sahi Tarika)
# Humne yahan 'client_id=' aur 'access_token=' likh diya hai 
# taaki 'positional argument' wala error hamesha ke liye khatam ho jaye
try:
    dhan = dhanhq(client_id=client_id, access_token=access_token)
    print("Dhan Connection Object Created! ✅")
except Exception as e:
    print(f"Initial Connection Error: {str(e)}")

def check_balance():
    print("--- SAMRAT AI TRADER ENGINE START ---")
    try:
        # 3. Account balance check karna
        # Dhan library mein fund check karne ka ye sahi tareeka hai
        funds = dhan.get_fund_limits()
        
        if funds.get('status') == 'success':
            data = funds.get('data', {})
            # Balance nikalne ki koshish (Alag alag keys check kar rahe hain)
            balance = data.get('availabelBalance') or data.get('availableBalance') or data.get('sodLimit', 0)
            print(f"SUCCESS: Aapka Dhan Balance hai: ₹{balance}")
        else:
            print(f"Dhan API Error: {funds.get('remarks', 'Invalid Credentials')}")
            
    except Exception as e:
        print(f"Technical Error while fetching balance: {str(e)}")

# --- SABSE ZAROORI: Yahan __name__ aur __main__ dhyan se dekhna ---
if __name__ == "__main__":
    check_balance()
