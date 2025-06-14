import allure
import pytest
from data import Data
from methods.orders_methods import OrdersMethods


class TestOrderCreate:

    @allure.title("Проверка возможности создания заказа с валидными ингредиентами")
    @pytest.mark.parametrize("auth_flag", [True, False])
    def test_order_create_positive(self, user_prepare, auth_flag):
        orders_methods = OrdersMethods()
        data = {'ingredients': orders_methods.ingredients_prepare()}
        order_number, response = orders_methods.order_create(data=data, access_token=user_prepare[1][0],
                                                             auth_flag=auth_flag)
        assert (response.status_code == 200) and \
               ('"success":true' in response.text) and \
               (order_number != -1), \
               f"status_code = {response.status_code}, text = {response.text}"

    @allure.title("Проверка невозможности создания заказа с невалидными ингредиентами")
    @pytest.mark.parametrize("auth_flag", [True, False])
    def test_order_create_for_invalid_ingredients(self, user_prepare, auth_flag):
        orders_methods = OrdersMethods()
        ingredients = orders_methods.ingredients_prepare()
        for index in range(len(ingredients)):
            ingredients[index] = "x" + ingredients[index] + "x"
        data = {'ingredients': ingredients}
        _, response = orders_methods.order_create(data=data, access_token=user_prepare[1][0],
                                                             auth_flag=auth_flag)
        assert (response.status_code == 500) and \
               ("Internal Server Error" in response.text), \
               f"status_code = {response.status_code}, text = {response.text}"

    @allure.title("Проверка невозможности создания заказа без ингредиентов")
    @pytest.mark.parametrize("auth_flag", [True, False])
    def test_order_create_for_empty_ingredients(self, user_prepare, auth_flag):
        orders_methods = OrdersMethods()
        data = {'ingredients': []}
        _, response = orders_methods.order_create(data=data, access_token=user_prepare[1][0],
                                                  auth_flag=auth_flag)
        assert (response.status_code == 400) and \
               (response.text == Data.CODE_400_TEXT_FOR_EMPTY_INGREDIENTS), \
               f"status_code = {response.status_code}, text = {response.text}"
