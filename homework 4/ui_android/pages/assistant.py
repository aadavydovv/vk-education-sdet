from ui_android.locators import LocatorsAssistant
from ui_android.pages.base import PageBase


class PageAssistant(PageBase):
    locators = LocatorsAssistant()

    def say(self, something):
        self.click(self.locators.BUTTON_INPUT)

        self.find(self.locators.INPUT_SAY).send_keys(something)
        self.driver.hide_keyboard()

        self.click(self.locators.BUTTON_SAY)

    def check_response(self, expected_text):
        self.find(self.locators.by_text(expected_text), f'got unexpected response\n'
                                                        f'(expected "{expected_text}" to be in it)')

    def select_suggestion(self, title):
        locator_suggestion = self.locators.by_text(title)
        self.click(locator_suggestion, swipe=True, locator_scroll=self.locators.SCROLL_SUGGESTIONS)

    def visit_settings(self):
        self.click(self.locators.BUTTON_SETTINGS)
