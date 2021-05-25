from ui_android.locators import LocatorsSettings
from ui_android.pages.base import PageBase


class PageSettings(PageBase):
    locators = LocatorsSettings()

    def visit_settings_news(self):
        self.click(self.locators.BUTTON_NEWS, swipe=True)

    def visit_settings_about(self):
        self.click(self.locators.BUTTON_ABOUT, swipe=True)
