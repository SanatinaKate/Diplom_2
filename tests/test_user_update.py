import allure
import pytest
from data import Data
from methods.user_methods import UserMethods


class TestUserUpdate:

    @allure.title("Проверка возможности успешного изменения данных пользователя с авторизацией")
    @pytest.mark.parametrize("key_updated", ['email', 'name'])
    def test_user_update_with_authorization(self, user_prepare, key_updated):
        user_data = dict(user_prepare[0])
        user_data[key_updated] = "updated_" + user_data[key_updated]
        user_methods = UserMethods()
        response = user_methods.user_update(data=user_data, access_token=user_prepare[1][0])
        assert (response.status_code == 200) and \
               ('"success":true' in response.text) and \
               (f'"{key_updated}":"{user_data[key_updated]}"' in response.text), \
               f"status_code = {response.status_code}, text = {response.text}"

    @allure.title("Проверка невозможности изменения данных пользователя без авторизации")
    @pytest.mark.parametrize("key_updated", ['email', 'name'])
    def test_user_update_without_authorization(self, user_prepare, key_updated):
        user_data = dict(user_prepare[0])
        user_data[key_updated] = "updated_" + user_data[key_updated]
        user_methods = UserMethods()
        response = user_methods.user_update(data=user_data, access_token=None)
        assert (response.status_code == 401) and \
               (response.text == Data.CODE_401_TEXT_FOR_UNAUTHORIZED_USER), \
               f"status_code = {response.status_code}, text = {response.text}"
