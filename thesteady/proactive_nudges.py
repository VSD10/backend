def send_nudge(user_id, context):
    # Implement nudge sending logic
    pass


from mentor_voice_engine import send_whatsapp_message
from message_handling import user_state

def send_weekly_recap(user_id):
    if user_id in user_state:
        income = user_state[user_id]["weekly_income"]
        saved = income * 0.1  # Simple calculation for demo
        message = f"Tumhare hafta ka hisaab 🌟\nKamaya: ₹{income}\nBachaya: ₹{saved}\nTum kar rahe ho!"
        send_whatsapp_message(user_id, message)
