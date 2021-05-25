import pytest
from _pytest.fixtures import FixtureRequest
from ui_android.pages.assistant import PageAssistant
from ui_android.pages.settings import PageSettings
from ui_android.pages.settings_about import PageSettingsAbout
from ui_android.pages.settings_news import PageSettingsNews


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, request: FixtureRequest):
        self.page_assistant: PageAssistant = request.getfixturevalue('page_assistant')
        self.page_settings: PageSettings = request.getfixturevalue('page_settings')
        self.page_settings_about: PageSettingsAbout = request.getfixturevalue('page_settings_about')
        self.page_settings_news: PageSettingsNews = request.getfixturevalue('page_settings_news')
