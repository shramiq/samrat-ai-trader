import pyotp
from dhanhq import dhanhq

# --- BHAI YAHAN APNI DETAILS DIRECT DALO ---
client_id = "1109242552" 
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzg2NTA3NjAzLCJpYXQiOjE3ODY0MjEyMDMsInRva2VuQ29uc3VtZXJUeXBlIjoiU0VMRiIsIndlYmhvb2tVcmwiOiIiLCJkaGFuQ2xpZW50SWQiOiIxMTA5MjQyNTUyIn0.AEWUKmVnNV2dNwMbgPqpAxMnhHSJKkeNIrgr5IGEE-er_GCufTB18GJ6uF6_xy_34HJ4gDXXQKD33LH3MbjDHg"
totp_seed = "FZW7Y5OZSGHYS62V4ZWGQIIIFB7DJZGG"

print("--- SAMRAT AI TRADER STARTING ---")

try:
    # 1. Live OTP Check
    totp = pyotp.TOTP(totp_seed)
    print(f"Robot Live OTP: {totp.now()} ✅")

    # 2. Dhan Connection (Basic Version)
    # Hum sirf wahi 2 cheezein bhej rahe hain jo library maang rahi hai
    dhan = dhanhq(client_id, access_token)
    print("Dhan Connection: OK ✅")

    # 3. Balance Check
    funds = dhan.get_fund_limits()
    if funds.get('status') == 'success':
        data = funds.get('data', {})
        bal = data.get('availabelBalance') or data.get('availableBalance') or 0
        print(f"SUCCESS! Aapka Balance hai: ₹{bal}")
    else:
        print("API Error:", funds.get('remarks'))

except Exception as e:
    print("Technical Error:", str(e))
