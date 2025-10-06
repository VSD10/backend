def parse_message(text):
    text = text.upper()
    if "EARN" in text:
        amount = extract_number(text)  # e.g., 800
        return {"type": "income", "amount": amount}
    elif "SPENT" in text:
        return {"type": "expense", "amount": extract_number(text)}


def extract_number(text):
    # Extract number from text
    import re
    numbers = re.findall(r'\d+', text)
    return int(numbers[0]) if numbers else 0


# In-memory user state (for hackathon demo purposes)
user_state = {}
