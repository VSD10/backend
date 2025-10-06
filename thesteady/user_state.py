USERS = {}  # In-memory; for persistent storage use SQLite

def get_user(user_id):
    if user_id not in USERS:
        USERS[user_id] = {'weekly_income': 0, 'weekly_saved': 0, 'last_earn': 0, 'language': 'hinglish'}
    return USERS[user_id]

def update_balance(user_id, income=None, expense=None, saved=None):
    user = get_user(user_id)
    if income:
        user['weekly_income'] += income
        user['last_earn'] = income
    if saved:
        user['weekly_saved'] += saved
    if expense:
        pass  # Expand as needed

def reset_week(user_id):
    user = get_user(user_id)
    user['weekly_income'] = 0
    user['weekly_saved'] = 0
