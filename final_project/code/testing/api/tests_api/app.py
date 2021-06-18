from cases.app import CaseAPIApp
import allure


@allure.epic('myapp api')
@allure.feature('app instance info')
class TestAPIApp(CaseAPIApp):

    @allure.title('get app status test')
    def test_app_status(self):
        """
        протестировать получение статуса приложения

        шаги:
            1) совершить запрос статуса приложения
            2) проверить ответ

        ответ должен иметь статус 200 - действие выполнено - с телом формата json, содержащее ключ "status" со значением "ok"
        """
        self.check_app_status()
