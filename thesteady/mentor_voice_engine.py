
import os
import requests
from nudges import NUDGES
from user_state import get_user, update_balance

def send_whatsapp_message(to, text):
    phone_number_id = os.getenv('PHONE_NUMBER_ID')
    whatsapp_token = os.getenv('WHATSAPP_TOKEN')
    
    url = f"https://graph.facebook.com/v18.0/{phone_number_id}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "text": {"body": text}
    }
    headers = {
        "Authorization": f"Bearer {whatsapp_token}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response

def generate_reply(user_id, context):
    user = get_user(user_id)
    lang = user.get('language', 'hinglish')
    
    if not context or "type" not in context:
        return "Main samajh nahi paaya. Phir se bhejo?"
    
    if context["type"] == "income":
        if context.get("amount", 0) <= 0:
            return "Kripya valid amount bataiye. Jaise 'EARN 500'."
        save_amt = min(30, int(context["amount"] * 0.03))
        update_balance(user_id, income=context["amount"], saved=save_amt)
        return NUDGES["save_after_income"][lang].format(
            amount=context["amount"], 
            save=save_amt
        )
    elif context["type"] == "expense":
        # Handle expense if needed
        pass
    return "Main samajh nahi paaya. Phir se bhejo?"
