import allure
import pytest
from data import Data
from methods.orders_methods import OrdersMethods


class TestOrdersList:

    @allure.title("Проверка возможности получения заказов для авторизованного пользователя")
    @pytest.mark.parametrize("orders_prepare", [1, 2, 3, 4, 5], indirect=True)
    def test_orders_list_positive(self, orders_prepare):
        orders_methods = OrdersMethods()
        orders, response = orders_methods.orders_get_list(access_token=orders_prepare[0])
        assert (response.status_code == 200) and \
               ('"success":true' in response.text) and \
               (orders == orders_prepare[1]), \
               f"status_code = {response.status_code}, text = {response.text}"

    @allure.title("Проверка невозможности получения заказов для неавторизованного пользователя")
    def test_orders_list_for_unauthorized_user(self, orders_prepare):
        orders_methods = OrdersMethods()
        _, response = orders_methods.orders_get_list(access_token=None)
        assert (response.status_code == 401) and \
               (response.text == Data.CODE_401_TEXT_FOR_UNAUTHORIZED_USER), \
               f"status_code = {response.status_code}, text = {response.text}"
