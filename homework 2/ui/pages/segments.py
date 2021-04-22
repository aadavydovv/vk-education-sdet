from datetime import datetime
from selenium.common.exceptions import TimeoutException
from ui.locators import LocatorsSegments
from ui.pages.base import PageBase
import allure
import pytest


class PageSegments(PageBase):
    url = 'https://target.my.com/segments/segments_list'
    locators = LocatorsSegments()

    @allure.step('creating a new segment')
    def create_segment(self):
        try:
            self.click(self.locators.BUTTON_CREATE_SUBSEQUENT_SEGMENT)

        except TimeoutException:
            self.click(self.locators.BUTTON_CREATE_FIRST_SEGMENT)

        self.click(self.locators.BUTTON_CHOOSE_SEGMENT_GROUP)
        self.click(self.locators.BUTTON_CHOOSE_SEGMENT)
        self.click(self.locators.BUTTON_ADD_SEGMENT)

        segment_name = f'segment from {datetime.now()}'
        self.input(self.locators.INPUT_SEGMENT_NAME, segment_name)

        self.click(self.locators.BUTTON_FINISH_CREATION)

        return segment_name

    @allure.step('deleting the segment "{segment_name}"')
    def delete_segment(self, segment_name):
        self.click(self.locators.entry_checkbox_by_title(segment_name, self.find))
        self.click(self.locators.BUTTON_ACTIONS)
        self.click(self.locators.BUTTON_DELETE_SEGMENT)
        self.find(self.locators.TEXT_SUCCESS)

    @allure.step('checking if the segment "{segment_name}" deletion was successful')
    def check_deletion(self, segment_name):
        with pytest.raises(TimeoutException):
            self.check_creation(segment_name)
