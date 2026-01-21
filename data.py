from uuid import uuid4

def generate_email():
    return f"{uuid4().hex}@example.com"

def generate_password():
    return "Test12345"

def generate_user_credentials():
    return {
        "email": generate_email(),
        "password": generate_password(),
    }

def get_ad_data():
    return {
        "title": "Палочка Гарри Поттера",
        "description": "Почти как у Олливандера. Заклинания не гарантируются",
        "price": "1199",
    }