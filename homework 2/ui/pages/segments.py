from datetime import datetime
from selenium.common.exceptions import TimeoutException
from ui.locators import LocatorsSegments
from ui.pages.base import PageBase
import allure
import pytest


class PageSegments(PageBase):
    url = 'https://target.my.com/segments/segments_list'
    locators = LocatorsSegments()
    nothing_to_delete = False

    @allure.step('creating a new segment')
    def create_segment(self):
        try:
            self.click(self.locators.BUTTON_CREATE_SUBSEQUENT_SEGMENT)

        except TimeoutException:
            self.click(self.locators.BUTTON_CREATE_FIRST_SEGMENT)

        self.click(self.locators.BUTTON_CHOOSE_SEGMENT_GROUP)
        self.click(self.locators.BUTTON_CHOOSE_SEGMENT)
        self.click(self.locators.BUTTON_ADD_SEGMENT)

        segment_name = str(datetime.now())
        self.input(self.locators.INPUT_SEGMENT_NAME, segment_name)
        self.new_segment_name = segment_name

        self.click(self.locators.BUTTON_FINISH_CREATION)

    @allure.step('checking if the new segment was created')
    def check_creation(self):
        self.find(self.locators.entry_by_title(self.new_segment_name),
                  'cannot find the new segment among the entries')

    @allure.step('deleting the first segment in the segments list')
    def delete_first_segment(self):
        if self.nothing_to_delete:
            return

        self.click(self.locators.BUTTON_FIRST_SEGMENT)
        self.click(self.locators.BUTTON_ACTIONS)
        self.click(self.locators.BUTTON_DELETE_SEGMENT)
        self.find(self.locators.TEXT_SUCCESS)

    @allure.step('checking if there is at least one segment to delete')
    def pre_delete_check(self, logger):
        try:
            self.title_first_segment = self.find(self.locators.TEXT_FIRST_SEGMENT).text

        except TimeoutException:
            logger.info('there are no segments to delete')
            self.nothing_to_delete = True

    @allure.step('checking if the segment deletion was successful')
    def post_delete_check(self):
        if self.nothing_to_delete:
            return

        self.driver.refresh()

        with pytest.raises(TimeoutException):
            self.find(self.locators.entry_by_title(self.title_first_segment))
