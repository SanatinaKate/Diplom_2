class Data:

    BASE_API_URL = "https://stellarburgers.nomoreparties.site/api"
    AUTH_URL = f"{BASE_API_URL}/auth"
    ORDERS_URL = f"{BASE_API_URL}/orders"

    CODE_400_TEXT_FOR_EMPTY_INGREDIENTS = '{"success":false,"message":"Ingredient ids must be provided"}'
    CODE_401_TEXT_FOR_UNAUTHORIZED_USER = '{"success":false,"message":"You should be authorised"}'
    CODE_401_TEXT_FOR_INVALID_FIELDS = '{"success":false,"message":"email or password are incorrect"}'
    CODE_403_TEXT_FOR_EXISTING_USER = '{"success":false,"message":"User already exists"}'
    CODE_403_TEXT_FOR_REQUIRED_FIELDS= '{"success":false,"message":"Email, password and name are required fields"}'
