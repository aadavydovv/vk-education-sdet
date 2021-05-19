from base import BaseCase
from mock.constants import *
import inspect
import pytest


class TestMock(BaseCase):

    @pytest.mark.Mock
    def test_add_user(self):
        user_id = inspect.currentframe().f_code.co_name  # не смог догадаться, как избавиться от сей копипасты :(

        response_put = self.client.put_user(user_id, self.name_first, self.name_last)
        assert (response_put['message']['id'],
                response_put['message']['name_first'],
                response_put['message']['name_last']) == (user_id, self.name_first, self.name_last)
        assert response_put['status'] == STATUS_CREATED

        response_get = self.client.get_user(user_id)['message']
        assert (response_get['name_first'], response_get['name_last']) == (self.name_first, self.name_last)

    @pytest.mark.Mock
    def test_add_user_without_last_name(self):
        user_id = inspect.currentframe().f_code.co_name

        response_put = self.client.put_user(user_id, self.name_first)['message']
        assert (response_put['id'], response_put['name_first']) == (user_id, self.name_first)

        response_get = self.client.get_user(user_id)['message']
        assert not response_get.get('name_last')

    @pytest.mark.Mock
    def test_add_user_without_first_name(self):
        user_id = inspect.currentframe().f_code.co_name

        assert self.client.put_user(user_id, '')['status'] == STATUS_BAD_REQUEST
        assert self.client.put_user(user_id, '', self.name_last)['status'] == STATUS_BAD_REQUEST
        assert self.client.get_user(user_id)['status'] == STATUS_ERROR

    @pytest.mark.Mock
    def test_edit_user(self):
        user_id = inspect.currentframe().f_code.co_name

        self.client.put_user(user_id, self.name_first, self.name_last)

        response_get = self.client.get_user(user_id)['message']
        assert (response_get['name_first'], response_get['name_last']) == (self.name_first, self.name_last)

        new_first_name = 'new first name'
        new_last_name = 'new last name'
        self.client.put_user(user_id, new_first_name, new_last_name)

        response_get = self.client.get_user(user_id)['message']
        assert (response_get['name_first'], response_get['name_last']) == (new_first_name, new_last_name)

    @pytest.mark.Mock
    def test_delete_user(self):
        user_id = inspect.currentframe().f_code.co_name

        self.client.put_user(user_id, self.name_first, self.name_last)

        assert self.client.get_user(user_id)['status'] == STATUS_OK

        delete_response = self.client.delete_user(user_id)['message']
        assert (delete_response['id'], delete_response['name_first'], delete_response['name_last']) ==\
               (user_id, self.name_first, self.name_last)

        assert self.client.get_user(user_id)['status'] == STATUS_ERROR

    @pytest.mark.Mock
    def test_delete_nonexistent_user(self):
        user_id = inspect.currentframe().f_code.co_name
        assert self.client.delete_user(user_id)['status'] == STATUS_ERROR
