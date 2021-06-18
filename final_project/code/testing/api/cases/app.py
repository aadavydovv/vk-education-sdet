from cases.base import CaseAPIBase
from misc.constants import STATUS_OK
import allure


class CaseAPIApp(CaseAPIBase):

    @allure.step('check the app status')
    def check_app_status(self):
        response = self.api_client.get_status()

        self.check_response_status(response, STATUS_OK)
        assert response.json()['status'] == 'ok'
