from datetime import datetime
from ui.locators import LocatorsCampaignCreation
from ui.pages.base import PageBase
import allure


class PageCampaignCreation(PageBase):
    url = 'https://target.my.com/campaign/new'
    locators = LocatorsCampaignCreation()

    @allure.step('creating a new campaign')
    def create_campaign(self, path_picture):
        self.click(self.locators.BUTTON_GOAL_TRAFFIC)
        self.input(self.locators.INPUT_AD_URL, 'education.mail.ru')
        self.click(self.locators.BUTTON_FORMAT_BANNER)
        self.input(self.locators.INPUT_PICTURE, path_picture, clear=False)

        campaign_name = f'campaign from {datetime.now()}'
        self.input(self.locators.INPUT_NAME, campaign_name)

        self.click(self.locators.BUTTON_FINISH_CREATION)
        self.find(self.locators.TEXT_SUCCESS)

        return campaign_name
