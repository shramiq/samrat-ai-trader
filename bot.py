import os
from dhanhq import dhanhq

# 1. GitHub Secrets se keys uthana
client_id = os.getenv('DHAN_CLIENT_ID')
access_token = os.getenv('DHAN_ACCESS_TOKEN')

def check_connection():
    print("--- SAMRAT AI TRADER ENGINE START ---")
    
    try:
        # 2. Dhan Connection (Sahi Tarika)
        # Hum seedha (Client ID, Access Token) bhej rahe hain bina keyword ke
        dhan = dhanhq(client_id, access_token)
        print("Dhan Connection Object Created! ✅")
        
        # 3. Account balance check karna
        funds = dhan.get_fund_limits()
        
        if funds.get('status') == 'success':
            data = funds.get('data', {})
            # Dhan ke different versions ke liye keys check karna
            balance = data.get('availabelBalance') or data.get('availableBalance') or 0
            print(f"SUCCESS: Aapka Dhan Balance hai: ₹{balance}")
        else:
            print("Galti: Dhan API ne response toh diya par success nahi hua.")
            print("Message:", funds.get('remarks', 'Check API Keys'))
            
    except Exception as e:
        print(f"Technical Error: {str(e)}")
        print("Tip: Check karein ki GitHub Secrets mein Client ID aur Token ekdam sahi hain.")

if _name_ == "_main_":
    check_connection()
