import random
import string

import allure

from data import TestAuthorizationData

class TestDataHelper:

    @staticmethod
    @allure.step("Генерация тела запроса для регистрации курьера")
    def generate_registration_body(random_login):
        body = TestAuthorizationData.CREATE_COURIER_BODY.copy()
        body['login'] = random_login
        return body

    @staticmethod
    @allure.step("Генерация тела запроса для авторизации курьера")
    def generate_login_body(random_login):
        body = TestAuthorizationData.LOGIN_COURIER_BODY.copy()
        body['login'] = random_login
        return body

    @staticmethod
    @allure.step("Генерация случайного логина")
    def generate_random_login():
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(8))