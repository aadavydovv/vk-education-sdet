from selenium.webdriver.common.by import By


class LocatorsBase:
    @staticmethod
    def by_text(text):
        return By.XPATH, f'//android.widget.TextView[contains(@text, "{text}")]'

    @staticmethod
    def by_element_for_marussia(element_name):
        return By.ID, f'ru.mail.search.electroscope:id/{element_name}'


# (здесь и далее) от LocatorsBase хоть наследовать и нечего - оставил, как формальность
class LocatorsAssistant(LocatorsBase):
    BUTTON_INPUT = LocatorsBase.by_element_for_marussia('keyboard')
    BUTTON_SAY = LocatorsBase.by_element_for_marussia('text_input_send')
    BUTTON_SETTINGS = LocatorsBase.by_element_for_marussia('assistant_menu_bottom')

    INPUT_SAY = LocatorsBase.by_element_for_marussia('input_text')
    SCROLL_SUGGESTIONS = LocatorsBase.by_element_for_marussia('suggests_list')


class LocatorsSettings(LocatorsBase):
    BUTTON_ABOUT = LocatorsBase.by_element_for_marussia('user_settings_about')
    BUTTON_NEWS = LocatorsBase.by_element_for_marussia('user_settings_field_news_sources')


class LocatorsSettingsAbout(LocatorsBase):
    TEXT_COPYRIGHT = LocatorsBase.by_element_for_marussia('about_copyright')
    TEXT_VERSION = LocatorsBase.by_element_for_marussia('about_version')


class LocatorsSettingsNews(LocatorsBase):
    # результат получается лишь в том случае, если кнопка с указанным названием отмечена выбранной
    @staticmethod
    def source_selected(title):
        return By.XPATH, f'{LocatorsBase.by_text(title)[1]}/../android.widget.ImageView'
