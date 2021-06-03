from base import BaseCase
from mock.constants import *
from mock.server import users
import inspect
import pytest


class TestMock(BaseCase):

    @pytest.mark.Mock
    def test_add_user_via_put(self):
        user_id = inspect.currentframe().f_code.co_name

        response_put = self.client.put_user(user_id, self.name_first, self.name_last)
        self.check_response(response_put, STATUS_CREATED, user_id, self.name_first, self.name_last)

        response_get = self.client.get_user(user_id)
        self.check_response(response_get, STATUS_OK, name_first=self.name_first, name_last=self.name_last)

    @pytest.mark.Mock
    def test_add_user_without_last_name(self):
        user_id = inspect.currentframe().f_code.co_name

        response_post = self.client.post_user(user_id, self.name_first)
        self.check_response(response_post, STATUS_CREATED, user_id, self.name_first, name_last_empty=True)

        response_get = self.client.get_user(user_id)
        self.check_response(response_get, STATUS_OK, name_first=self.name_first, name_last_empty=True)

    @pytest.mark.Mock
    def test_add_user_without_first_name_via_put(self):
        user_id = inspect.currentframe().f_code.co_name

        response_put = self.client.put_user(user_id, '')
        self.check_response(response_put, STATUS_BAD_REQUEST)

        response_get = self.client.get_user(user_id)
        self.check_response(response_get, STATUS_ERROR)

    @pytest.mark.Mock
    def test_edit_user(self):
        user_id = inspect.currentframe().f_code.co_name

        users[user_id] = {'name_first': self.name_first, 'name_last': self.name_last}

        new_first_name = self.faker_instance.first_name()
        new_last_name = self.faker_instance.last_name()

        response_put = self.client.put_user(user_id, new_first_name, new_last_name)
        self.check_response(response_put, STATUS_OK, user_id, new_first_name, new_last_name)

        response_get = self.client.get_user(user_id)
        self.check_response(response_get, STATUS_OK, name_first=new_first_name, name_last=new_last_name)

    @pytest.mark.Mock
    def test_delete_user(self):
        user_id = inspect.currentframe().f_code.co_name

        users[user_id] = {'name_first': self.name_first, 'name_last': self.name_last}

        response_delete = self.client.delete_user(user_id)
        self.check_response(response_delete, STATUS_OK, user_id, self.name_first, self.name_last)

        response_get = self.client.get_user(user_id)
        self.check_response(response_get, STATUS_ERROR)

    @pytest.mark.Mock
    def test_delete_nonexistent_user(self):
        user_id = inspect.currentframe().f_code.co_name

        response_delete = self.client.delete_user(user_id)
        self.check_response(response_delete, STATUS_ERROR)

    @pytest.mark.Mock
    def test_add_user_via_post(self):
        user_id = inspect.currentframe().f_code.co_name

        response_post = self.client.post_user(user_id, self.name_first, self.name_last)
        self.check_response(response_post, STATUS_CREATED, user_id, self.name_first, self.name_last)

        response_get = self.client.get_user(user_id)
        self.check_response(response_get, STATUS_OK, name_first=self.name_first, name_last=self.name_last)

    @pytest.mark.Mock
    def test_add_existing_user(self):
        user_id = inspect.currentframe().f_code.co_name

        users[user_id] = {'name_first': self.name_first, 'name_last': self.name_last}

        response_post = self.client.post_user(user_id, self.name_first, self.name_last)
        self.check_response(response_post, STATUS_ERROR)

    @pytest.mark.Mock
    def test_edit_user_with_empty_input(self):
        user_id = inspect.currentframe().f_code.co_name

        users[user_id] = {'name_first': self.name_first, 'name_last': self.name_last}

        response_put = self.client.put_user(user_id, '')
        self.check_response(response_put, STATUS_BAD_REQUEST)

    @pytest.mark.Mock
    def test_add_user_without_first_name_via_post(self):
        user_id = inspect.currentframe().f_code.co_name

        response_post = self.client.post_user(user_id, '')
        self.check_response(response_post, STATUS_BAD_REQUEST)

        response_get = self.client.get_user(user_id)
        self.check_response(response_get, STATUS_ERROR)
