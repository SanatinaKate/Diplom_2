import allure
import requests
from data import Data
from helpers import Helpers


class UserMethods:

    @allure.step("Зарегистрировать пользователя")
    def user_register(self, data=None, raise_error=False):
        user_data = Helpers.generate_random_user() if data is None else dict(data)
        response = requests.post(url=f"{Data.AUTH_URL}/register", data=user_data)
        if response.status_code == 200:
            tokens = [response.json()['accessToken'], response.json()['refreshToken']]
        elif not raise_error:
            user_data = {}
            tokens = []
        else:
            raise AssertionError("Не удалось зарегистрировать пользователя")
        return user_data, tokens, response

    @allure.step("Авторизовать пользователя")
    def user_login(self, data, raise_error=False):
        user_data = dict(data)
        if 'name' in user_data.keys():
            del user_data['name']
        response = requests.post(url=f"{Data.AUTH_URL}/login", data=user_data)
        if response.status_code == 200:
            tokens = [response.json()['accessToken'], response.json()['refreshToken']]
        elif not raise_error:
            tokens = []
        else:
            raise AssertionError("Не удалось авторизовать пользователя")
        return tokens, response

    @allure.step("Изменить данные пользователя")
    def user_update(self, data, access_token):
        user_data = dict(data)
        if 'password' in user_data.keys():
            del user_data['password']
        if access_token is not None:
            headers = {'Authorization': access_token}
            response = requests.patch(url=f"{Data.AUTH_URL}/user", headers=headers, data=user_data)
        else:
            response = requests.patch(url=f"{Data.AUTH_URL}/user", data=user_data)
        return response

    @allure.step("Удалить пользователя")
    def user_delete(self, access_token):
        headers = {'Authorization': access_token}
        response = requests.delete(url=f"{Data.AUTH_URL}/user", headers=headers)
        return response
