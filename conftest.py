import pytest
from methods.orders_methods import  OrdersMethods
from methods.user_methods import UserMethods


# Фикстура для регистрации/удаления пользователя
@pytest.fixture
def user_prepare():
    user_methods = UserMethods()
    user_data, tokens, _ = user_methods.user_register(raise_error=True)
    yield user_data, tokens
    user_methods.user_delete(access_token=tokens[0])

# Фикстура для создания заказов
@pytest.fixture(params=[1])
def orders_prepare(request, user_prepare):
    orders = []
    access_token = user_prepare[1][0]
    orders_methods = OrdersMethods()
    for _ in range(request.param):
        data = {'ingredients': orders_methods.ingredients_prepare()}
        order, _ = orders_methods.order_create(data=data, access_token=access_token, auth_flag=True, raise_error=True)
        orders.append(order)
    return access_token, orders
