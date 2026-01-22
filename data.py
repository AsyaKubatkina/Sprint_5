from uuid import uuid4

PASSWORD = "Test12345"

AD_TITLE = "Палочка Гарри Поттера"
AD_DESCRIPTION = "Почти как у Олливандера. Заклинания не гарантируются"
AD_PRICE = "1199"

def generate_email():
    return f"{uuid4().hex}@example.com"


