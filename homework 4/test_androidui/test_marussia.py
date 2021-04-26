from test_androidui.base import BaseCase
import pytest


class TestCommand(BaseCase):
    @pytest.mark.AndroidUI
    def test_say_russia(self):
        self.page_assistant.say('Russia')
        self.page_assistant.check_response('государство в Восточной Европе и Северной Азии')

        self.page_assistant.select_suggestion('численность населения россии')
        self.page_assistant.check_response('146 млн')

    @pytest.mark.AndroidUI
    def test_calculate(self):
        self.page_assistant.say('13 + 37')
        self.page_assistant.check_response('50')


class TestSettings(BaseCase):
    @pytest.mark.AndroidUI
    def test_news_sources(self):
        self.page_assistant.visit_settings()
        self.page_settings.visit_settings_news()

        title_news_source = 'Вести FM'

        self.page_settings_news.choose_source(title_news_source)
        self.page_settings_news.check_source_choice(title_news_source)

        self.page_settings_news.visit_assistant()

        self.page_assistant.say('News')
        self.page_assistant.check_response(f'Включаю новости {title_news_source}')

    @pytest.mark.AndroidUI
    def test_about(self):
        self.page_assistant.visit_settings()
        self.page_settings.visit_settings_about()

        self.page_settings_about.check_versions()
        self.page_settings_about.check_trademark()
