import allure
import pytest
from data import Data
from methods.user_methods import UserMethods


class TestUserLogin:

    @allure.title("Проверка возможности успешной авторизации пользователя")
    def test_user_login_positive(self, user_prepare):
        user_methods = UserMethods()
        tokens, response = user_methods.user_login(data=user_prepare[0])
        assert (response.status_code == 200) and \
               ('"success":true' in response.text) and \
               (len(tokens) == 2), \
               f"status_code = {response.status_code}, text = {response.text}"

    @allure.title("Проверка невозможности авторизации пользователя с невалидными данными")
    @pytest.mark.parametrize("key_invalid", ['email', 'password'])
    def test_user_login_for_invalid_data(self, user_prepare, key_invalid):
        user_methods = UserMethods()
        user_data = dict(user_prepare[0])
        user_data[key_invalid] = "_" + user_data[key_invalid]
        _, response = user_methods.user_login(data=user_data)
        assert (response.status_code == 401) and \
               (response.text == Data.CODE_401_TEXT_FOR_INVALID_FIELDS), \
               f"status_code = {response.status_code}, text = {response.text}"
