import allure


class CaseUIBase:

    @allure.step('set up the "base ui" test case')
    def setup_base(self, driver, logger):
        self.driver = driver
        self.logger = logger

        self.logger.info('completed the "base ui" test case setup')
