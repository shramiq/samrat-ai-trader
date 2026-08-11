import os
import pyotp
from dhanhq import dhanhq

def run_engine():
    print("--- SAMRAT AI TRADER STARTING ---")
    
    # 1. Secrets uthana
    cid = os.getenv('DHAN_CLIENT_ID')
    tok = os.getenv('DHAN_ACCESS_TOKEN')
    seed = os.getenv('DHAN_TOTP_KEY')

    if not seed:
        print("Error: DHAN_TOTP_KEY nahi mila!")
        return

    try:
        # 2. OTP Generate karna
        totp = pyotp.TOTP(seed)
        current_otp = totp.now()
        print(f"Robot Live OTP: {current_otp} ✅")

        # 3. Dhan Connection
        dhan = dhanhq(cid, tok)
        
        # 4. Balance Check
        funds = dhan.get_fund_limits()
        if funds.get('status') == 'success':
            data = funds.get('data', {})
            balance = data.get('availabelBalance') or data.get('availableBalance') or 0
            print(f"SUCCESS! Connection OK. Account Balance: ₹{balance}")
        else:
            print(f"Dhan API Message: {funds.get('remarks')}")

    except Exception as e:
        print(f"Galti: {str(e)}")

if _name_ == "_main_":
    run_engine()
