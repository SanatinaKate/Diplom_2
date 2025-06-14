import allure
import pytest
from data import Data
from helpers import Helpers
from methods.user_methods import UserMethods


class TestUserRegister:

    @allure.title("Проверка возможности успешной регистрации пользователя")
    def test_user_register_positive(self):
        user_methods = UserMethods()
        _, tokens, response = user_methods.user_register()
        assert (response.status_code == 200) and \
               ('"success":true' in response.text) and \
               (len(tokens) == 2), \
               f"status_code = {response.status_code}, text = {response.text}"

    @allure.title("Проверка невозможжости регистрации уже зарегистрированного пользователя")
    def test_user_register_for_existing_email(self):
        user_methods = UserMethods()
        user_data, _, _ = user_methods.user_register()
        user_data_2 = {
            'email': user_data['email'],
            'password': Helpers.generate_random_string(8),
            'name': Helpers.generate_random_string(8)
        }
        _, _, response = user_methods.user_register(data=user_data_2)
        assert (response.status_code == 403) and \
               (response.text == Data.CODE_403_TEXT_FOR_EXISTING_USER), \
               f"status_code = {response.status_code}, text = {response.text}"

    @allure.title("Проверка невозможности регистрации пользователя без передачи всех обязательных полей")
    @pytest.mark.parametrize("key_missing", ["email", "password", "name"])
    def test_user_register_for_incomplete_data(self, key_missing):
        user_data =Helpers.generate_random_user()
        del user_data[key_missing]
        user_methods = UserMethods()
        _, _, response = user_methods.user_register(data=user_data)
        assert (response.status_code == 403) and \
               (response.text == Data.CODE_403_TEXT_FOR_REQUIRED_FIELDS), \
               f"status_code = {response.status_code}, text = {response.text}"
