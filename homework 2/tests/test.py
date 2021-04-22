from tests.base import BaseCase
import allure
import pytest


class TestAuth(BaseCase):
    @pytest.mark.UI
    @allure.story('негативные тесты на авторизацию')
    def test_incorrect_login(self, page_auth):
        page_auth.log_in(self.config, login='0')
        page_auth.check_failed_auth_by_locator()

    @pytest.mark.UI
    @allure.story('негативные тесты на авторизацию')
    def test_incorrect_password(self, page_auth):
        page_auth.log_in(self.config, password='0')
        page_auth.check_failed_auth_by_url()


class TestCampaignCreation(BaseCase):
    @pytest.mark.UI
    @allure.story('тест на создание рекламной кампании')
    def test_campaign_creation(self, page_campaign_creation, path_picture):
        new_campaign_name = page_campaign_creation.create_campaign(path_picture)
        page_campaign_creation.check_creation(new_campaign_name)


class TestSegments(BaseCase):
    @pytest.mark.UI
    @allure.story('тест на создание сегмента')
    def test_segment_create(self, page_segments):
        new_segment_name = page_segments.create_segment()
        page_segments.check_creation(new_segment_name)
        return new_segment_name

    @pytest.mark.UI
    @allure.story('тест на удаление сегмента')
    def test_segment_delete(self, page_segments):
        new_segment_name = self.test_segment_create(page_segments)
        page_segments.delete_segment(new_segment_name)
        page_segments.check_deletion(new_segment_name)
