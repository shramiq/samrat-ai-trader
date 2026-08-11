import os
from dhanhq import dhanhq

# 1. GitHub Secrets se keys uthana
client_id = os.getenv('DHAN_CLIENT_ID')
access_token = os.getenv('DHAN_ACCESS_TOKEN')

# 2. Dhan Connection (Sahi aur Final Tarika)
# Dhan library ko 'money' likh kar batana padta hai ki ye asli account hai
try:
    dhan = dhanhq(client_id, access_token, "money")
    print("Dhan Connection Object Created! ✅")

    print("--- SAMRAT AI TRADER ENGINE STARTING ---")
    
    # 3. Account balance check karna
    funds = dhan.get_fund_limits()
    
    if funds.get('status') == 'success':
        data = funds.get('data', {})
        # Alag-alag version ke liye balance check
        balance = data.get('availabelBalance') or data.get('availableBalance') or 0
        print(f"SUCCESS: Aapka Dhan Balance hai: ₹{balance}")
    else:
        print("API Error:", funds.get('remarks', 'Invalid Credentials'))

except Exception as e:
    print("Technical Error:", str(e))
