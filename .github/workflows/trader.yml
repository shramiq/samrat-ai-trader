import os
import pyotp
from dhanhq import dhanhq

# 1. GitHub Secrets se saari chabiyaan nikalna
client_id = os.getenv('DHAN_CLIENT_ID')
access_token = os.getenv('DHAN_ACCESS_TOKEN')
totp_key = os.getenv('DHAN_TOTP_KEY')

def start_samrat_engine():
    print("--- SAMRAT AI TRADER: INITIALIZING ---")
    
    # 2. Live OTP generate karna (TOTP)
    try:
        totp = pyotp.TOTP(totp_key)
        current_otp = totp.now()
        print(f"Robot ne Live OTP generate kiya: {current_otp} ✅")
    except Exception as e:
        print(f"OTP Error: {str(e)}")
        return

    # 3. Dhan Connection Setup
    try:
        # Dhan library ko 'client_id' aur 'access_token' bhej rahe hain
        dhan = dhanhq(client_id, access_token)
        
        # Account Balance Check karna tasalli ke liye
        funds = dhan.get_fund_limits()
        
        if funds.get('status') == 'success':
            data = funds.get('data', {})
            balance = data.get('availabelBalance') or data.get('availableBalance') or 0
            print(f"CONNECTION SUCCESSFUL! ✅")
            print(f"Aapke Dhan Account mein Balance: ₹{balance}")
            print("AI Agent market scanning ke liye taiyar hai...")
        else:
            print("DHAN API ERROR: Token shayad expire ho gaya hai.")
            print("Dhan Message:", funds.get('remarks'))

    except Exception as e:
        print(f"Technical Error: {str(e)}")

if _name_ == "_main_":
    start_samrat_engine()
