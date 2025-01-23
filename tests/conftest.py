import pytest

from helpers import TestDataHelper
from scooter_api import ScooterApi


@pytest.fixture(scope="function")
def delete_user():
    def _delete_user(id_):
        login_response = ScooterApi.login_courier(
            TestDataHelper.generate_login_body(id_)
        )
        user_id = login_response.json()['id']
        ScooterApi.delete_courier(user_id)
    yield _delete_user


@pytest.fixture(scope="function")
def create_and_delete_user(delete_user):
    rand_login = {"key": None}
    def _create_user(id_):
        ScooterApi.create_courier(TestDataHelper.generate_registration_body(id_))
        rand_login["key"] = id_
    yield _create_user
    delete_user(rand_login["key"])
