import allure
import random
import requests
from data import Data


class OrdersMethods:

    @allure.step("Подготовить список ингредиентов")
    def ingredients_prepare(self):
        response = requests.get(url=f"{Data.BASE_API_URL}/ingredients")
        if response.status_code == 200:
            ingredients = []
            data = response.json()['data']
            length = len(data)
            for index in random.sample(range(length), int(length * 0.2)):
                ingredients.append(data[index]['_id'])
            return ingredients
        else:
            raise AssertionError("Не удалось подготовить список ингредиентов")

    @allure.step("Создать заказ")
    def order_create(self, data, access_token, auth_flag, raise_error=False):
        order = -1
        if auth_flag:
            headers = {'Authorization': access_token}
            response = requests.post(url=Data.ORDERS_URL, headers=headers, data=data)
        else:
            response = requests.post(url=Data.ORDERS_URL, data=data)
        if response.status_code == 200:
            order = response.json()['order']['number']
        elif raise_error:
            raise AssertionError("Не удалось создать заказ")
        return order, response

    @allure.step("Получить список заказов пользователя")
    def orders_get_list(self, access_token):
        orders = []
        if access_token is not None:
            headers = {'Authorization': access_token}
            response = requests.get(url=Data.ORDERS_URL, headers=headers)
        else:
            response = requests.get(url=Data.ORDERS_URL)
        if response.status_code == 200:
            orders = []
            for order in response.json()['orders']:
                orders.append(order['number'])
        return orders, response
