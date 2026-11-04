import random
import string

class UserGenerator:
    @staticmethod
    def random_string(length=10):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    @staticmethod
    def generate_user_payload():
        first_name = UserGenerator.random_string()
        last_name = UserGenerator.random_string()
        user_name = UserGenerator.random_string()
        email = f"test_{UserGenerator.random_string()}@yandex.ru"
        password = UserGenerator.random_string()
        return first_name, last_name, user_name, email, password
