from selenium.common.exceptions import TimeoutException
from ui.locators import LocatorsPostAuth
from ui.pages.base import PageBase
from ui.pages.campaign_creation import PageCampaignCreation
from ui.pages.segments import PageSegments
import allure


class PagePostAuth(PageBase):
    url = 'https://target.my.com/dashboard'
    locators = LocatorsPostAuth()

    @allure.step('visiting segments')
    def visit_segments(self):
        self.click(self.locators.BUTTON_SEGMENTS)
        return PageSegments(self.driver)

    @allure.step('starting a new campaign creation')
    def start_campaign_creation(self):
        try:
            self.click(self.locators.BUTTON_CREATE_CAMPAIGN_SUBSEQUENT)

        except TimeoutException:
            self.click(self.locators.BUTTON_CREATE_CAMPAIGN_FIRST)

        return PageCampaignCreation(self.driver)
