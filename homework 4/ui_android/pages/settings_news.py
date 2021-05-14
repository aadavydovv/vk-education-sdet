from ui_android.locators import LocatorsSettingsNews
from ui_android.pages.base import PageBase


class PageSettingsNews(PageBase):
    locators = LocatorsSettingsNews()

    def choose_source(self, title):
        self.click(self.locators.by_text(title))

    def check_source_choice(self, title):
        self.find(self.locators.source_selected(title))

    def visit_assistant(self):
        for _ in range(2):
            self.driver.back()
