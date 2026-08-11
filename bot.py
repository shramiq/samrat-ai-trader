import os
from dhanhq import dhanhq

# 1. Chabi uthana
access_token = os.getenv('DHAN_ACCESS_TOKEN')
client_id = os.getenv('DHAN_CLIENT_ID')

# 2. Dhan Connection (Sahi Tarika)
# Error ke mutabiq library ko sirf 1 chiz chahiye: access_token
try:
    dhan = dhanhq(access_token)
    print("Dhan Connection Object Created! ✅")

    print("--- SAMRAT AI TRADER ENGINE STARTING ---")
    
    # 3. Account balance check karna
    funds = dhan.get_fund_limits()
    
    if funds.get('status') == 'success':
        data = funds.get('data', {})
        # Balance nikalne ka rasta
        balance = data.get('availabelBalance') or data.get('availableBalance') or 0
        print(f"SUCCESS: Aapka Dhan Balance hai: ₹{balance}")
    else:
        print("Dhan API Error:", funds.get('remarks', 'Invalid Token'))

except Exception as e:
    print("Technical Error:", str(e))
