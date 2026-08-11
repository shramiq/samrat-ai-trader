import os
from dhanhq import dhanhq

# 1. GitHub Secrets se keys uthana
client_id = os.getenv('DHAN_CLIENT_ID')
access_token = os.getenv('DHAN_ACCESS_TOKEN')

# 2. Dhan Connection
# Error ke mutabiq library ko sirf access_token chahiye
try:
    dhan = dhanhq(client_id, access_token)
    print("Dhan Connection Object Created! ✅")
except TypeError:
    # Agar upar wala fail ho, toh sirf token ke saath try karega
    dhan = dhanhq(access_token)
    print("Dhan Connection Object Created with Token! ✅")

def check_balance():
    print("--- SAMRAT AI TRADER ENGINE START ---")
    try:
        # 3. Account balance check karna
        funds = dhan.get_fund_limits()
        
        if funds.get('status') == 'success':
            data = funds.get('data', {})
            # Balance nikalne ki koshish
            balance = data.get('availabelBalance') or data.get('availableBalance') or 0
            print(f"SUCCESS: Aapka Dhan Balance hai: ₹{balance}")
        else:
            print(f"API Error: {funds.get('remarks', 'Check Credentials')}")
            
    except Exception as e:
        print(f"Technical Error: {str(e)}")

# --- DHAYAN DEIN: Yahan 2-2 dash (__) lagaye hain ---
if __name__ == "__main__":
    check_balance()
