
from flask import Flask, request
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

PHONE_NUMBER_ID = os.getenv('PHONE_NUMBER_ID')
WHATSAPP_TOKEN = os.getenv('WHATSAPP_TOKEN')

@app.route('/', methods=['GET'])
def index():
    return "Welcome to THESTEADY!"

@app.route('/webhook', methods=['GET'])
def verify():
    # Verify webhook
    return request.args.get('hub.challenge')


@app.route('/webhook', methods=['POST'])
def handle_message():
    data = request.get_json()
    
    # Validate webhook data structure
    if not data or 'entry' not in data or not data['entry']:
        return "Invalid webhook data structure", 400
    entry_data = data['entry'][0]
    if 'changes' not in entry_data or not entry_data['changes']:
        return "Invalid webhook data structure", 400
    changes_data = entry_data['changes'][0]
    if 'value' not in changes_data:
        return "Invalid webhook data structure", 400
    entry = changes_data['value']
    if 'messages' not in entry or not entry['messages']:
        return "No messages in webhook", 200
    
    # Extract user ID and message type
    user_id = entry['messages'][0]['from']
    msg_type = entry['messages'][0]['type']
    
    if msg_type == 'text':
        text = entry['messages'][0]['text']['body']

    elif msg_type == 'image':
        from image_and_voice import parse_image
        text = parse_image(entry['messages'][0]['image']['link'])
    elif msg_type == 'audio':
        from image_and_voice import parse_voice
        text = parse_voice(entry['messages'][0]['audio']['link'])
    else:
        text = "I can only process text, image, or audio messages for now."
    
    # Parse message
    from message_handling import parse_message
    context = parse_message(text)
    
    # Generate and send reply
    from mentor_voice_engine import generate_reply, send_whatsapp_message
    reply = generate_reply(user_id, context)
    send_whatsapp_message(user_id, reply)
    
    return "OK", 200

if __name__ == '__main__':
    app.run()
