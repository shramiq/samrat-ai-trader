import os
from dhanhq import dhanhq

# 1. GitHub Secrets se keys uthana
client_id = os.getenv('DHAN_CLIENT_ID')
access_token = os.getenv('DHAN_ACCESS_TOKEN')

# 2. Dhan Connection (Sahi Tarika)
# Hum bina keyword ke bhej rahe hain: Client ID aur Access Token
try:
    dhan = dhanhq(client_id, access_token)
    print("Dhan Connection Object Created! ✅")
    
    # 3. Account balance check karna
    print("--- SAMRAT AI TRADER ENGINE STARTING ---")
    funds = dhan.get_fund_limits()
    
    if funds.get('status') == 'success':
        data = funds.get('data', {})
        # Alag-alag version ke liye balance check
        balance = data.get('availabelBalance') or data.get('availableBalance') or 0
        print(f"SUCCESS: Aapka Dhan Balance hai: ₹{balance}")
    else:
        print("Dhan API Error:", funds.get('remarks', 'Invalid Credentials'))

except Exception as e:
    print("Technical Error:", str(e))
