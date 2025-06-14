import random
import string


class Helpers:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    @staticmethod
    def generate_random_user():
        name = Helpers.generate_random_string(7)
        user = {
            'email': f"{name}@{random.choice(['mail.ru', 'rambler.ru', 'yandex.ru'])}",
            'password': Helpers.generate_random_string(7),
            'name': name
        }
        return user
