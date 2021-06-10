from cases.home import CaseUIHome
from misc.constants import CONTROL_USER_USERNAME, CONTROL_USER_ID
import allure
import pytest


@allure.epic('myapp ui')
@allure.feature('home page')
class TestUIHome(CaseUIHome):

    @allure.title('logout test')
    def test_logout(self):
        """
        протестировать логаут

        шаги:
            1) кликнуть ссылку "logout"
            2) проверить, что url открывшейся страницы равен url страницы логина

        url должен быть следующим: "http://myapp/login"
        """
        self.page_home.log_out()
        self.check_url(self.page_login_url)

    @allure.title('login info (username) test')
    def test_login_info_username(self):
        """
        проверить имя пользователя в правом верхнем углу страницы

        шаги:
            1) найти элемент с информацией об авторизированном пользователе
            2) проверить текст элемента

        в тексте должно быть следующее: "Logged as юзернейм_контрольного_пользователя"
        """
        self.page_home.check_login_info(user_name=CONTROL_USER_USERNAME)

    @allure.title('login info (vk id) test')
    def test_login_info_id(self):
        """
        проверить id в правом верхнем углу страницы

        шаги:
            1) найти элемент с информацией об авторизированном пользователе
            2) проверить текст элемента

        в тексте должно быть следующее: "VK ID: id_контрольного_пользователя"
        """
        self.page_home.check_login_info(user_id=CONTROL_USER_ID)

    @allure.title('presence of a motivational fact test')
    def test_presence_of_fact(self):
        """
        проверить наличие мотивационного факта

        шаги:
            1) найти элемент с мотивационным фактом

        найденный элемент должен содержать какой-либо текст
        """
        self.page_home.find(self.page_home.locators.TEXT_FACT,
                            message='a motivational fact was not found')

    @allure.title('"home" link click test')
    def test_link_home(self):
        """
        протестировать ссылку "home"

        шаги:
            1) кликнуть ссылку "home"
            2) проверить, что url открывшейся страницы равен url домашней страницы

        url должен быть следующим: "http://myapp/welcome/"
        """
        self.page_home.click(self.page_home.locators.LINK_HOME)
        self.check_url(self.page_home.url)

    @allure.title('"python" link click test')
    def test_link_python(self):
        """
        протестировать ссылку "python"

        шаги:
            1) кликнуть ссылку "python"
            2) проверить, что url открывшейся страницы равен необходимому url

        url должен быть следующим: "https://www.python.org/"
        """
        self.page_home.click(self.page_home.locators.MENU_PYTHON)
        self.check_url('https://www.python.org/')

    @allure.title('"python - history" link click test')
    def test_link_python_history(self):
        """
        протестировать ссылку "python history" в меню "python"

        шаги:
            1) открыть меню "python"
            2) кликнуть ссылку "python history"
            3) проверить, что url открывшейся страницы равен необходимому url

        url должен быть следующим: "https://en.wikipedia.org/wiki/History_of_Python"
        """
        self.page_home.open_menu(self.page_home.locators.MENU_PYTHON)
        self.page_home.click(self.page_home.locators.LINK_PYTHON_HISTORY)
        self.check_url('https://en.wikipedia.org/wiki/History_of_Python')

    @allure.title('"python - about flask" link click test')
    def test_link_python_about_flask(self):
        """
        протестировать ссылку "about flask" в меню "python"

        шаги:
            1) открыть меню "python"
            2) кликнуть ссылку "about flask"
            3) переключиться на открывшуюся вкладку
            4) проверить, что url открывшейся страницы равен необходимому url

        url должен быть следующим: "https://flask.palletsprojects.com/en/1.1.x/#"
        """
        self.page_home.open_menu(self.page_home.locators.MENU_PYTHON)
        self.page_home.click(self.page_home.locators.LINK_ABOUT_FLASK)
        self.switch_to_last_opened_tab()
        self.check_url('https://flask.palletsprojects.com/en/1.1.x/#')

    @allure.title('"linux - download centos" link click test')
    def test_link_linux_download_centos(self):
        """
        протестировать ссылку "download centos7" в меню "linux"

        шаги:
            1) открыть меню "linux"
            2) кликнуть ссылку "download centos7"
            3) проверить, что url открывшейся страницы равен необходимому url

        url должен быть следующим: "https://www.centos.org/download/" (вероятно)
        """
        self.page_home.open_menu(self.page_home.locators.MENU_LINUX)
        self.page_home.click(self.page_home.locators.LINK_DOWNLOAD_CENTOS)
        self.switch_to_last_opened_tab()

        self.check_url('https://www.centos.org/download/')

    @allure.title('"network - wireshark news" link click test')
    def test_link_network_wireshark_news(self):
        """
        протестировать ссылку "news" в разделе "wireshark" меню "network"

        шаги:
            1) открыть меню "network"
            2) кликнуть ссылку "news" в разделе "wireshark"
            3) проверить, что url открывшейся страницы равен необходимому url

        url должен быть следующим: "https://www.wireshark.org/news/"
        """
        self.page_home.open_menu(self.page_home.locators.MENU_NETWORK)
        self.page_home.click(self.page_home.locators.LINK_WIRESHARK_NEWS)
        self.switch_to_last_opened_tab()
        self.check_url('https://www.wireshark.org/news/')

    @allure.title('"network - wireshark download" link click test')
    def test_link_network_wireshark_download(self):
        """
        протестировать ссылку "download" в разделе "wireshark" меню "network"

        шаги:
            1) открыть меню "network"
            2) кликнуть ссылку "download" в разделе "wireshark"
            3) проверить, что url открывшейся страницы равен необходимому url

        url должен быть следующим: "https://www.wireshark.org/#download"
        """
        self.page_home.open_menu(self.page_home.locators.MENU_NETWORK)
        self.page_home.click(self.page_home.locators.LINK_WIRESHARK_DOWNLOAD)
        self.switch_to_last_opened_tab()
        self.check_url('https://www.wireshark.org/#download')

    @allure.title('"network - tcpdump examples" link click test')
    def test_link_network_tcpdump_examples(self):
        """
        протестировать ссылку "examples" в разделе "tcpdump" меню "network"

        шаги:
            1) открыть меню "network"
            2) кликнуть ссылку "examples" в разделе "tcpdump"
            3) проверить, что url открывшейся страницы равен необходимому url

        url должен быть следующим: "https://hackertarget.com/tcpdump-examples/"
        """
        self.page_home.open_menu(self.page_home.locators.MENU_NETWORK)
        self.page_home.click(self.page_home.locators.LINK_TCPDUMP_EXAMPLES)
        self.switch_to_last_opened_tab()
        self.check_url('https://hackertarget.com/tcpdump-examples/')

    @allure.title('"what is api" link click test')
    def test_link_what_is_api(self):
        """
        протестировать ссылку "what is an api?"

        шаги:
            1) кликнуть ссылку "what is an api?"
            2) проверить, что url открывшейся страницы равен необходимому url

        url должен быть следующим: "https://en.wikipedia.org/wiki/API"
        """
        self.page_home.click(self.page_home.locators.LINK_WHAT_IS_API)
        self.switch_to_last_opened_tab()
        self.check_url('https://en.wikipedia.org/wiki/API')

    @allure.title('"future of internet" link click test')
    def test_link_future_of_internet(self):
        """
        протестировать ссылку "future of internet"

        шаги:
            1) кликнуть ссылку "future of internet"
            2) проверить, что url открывшейся страницы равен необходимому url

        url должен быть следующим: "https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/"
        """
        self.page_home.click(self.page_home.locators.LINK_FUTURE_OF_INTERNET)
        self.switch_to_last_opened_tab()
        self.check_url('https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/')

    @allure.title('"about smtp" link click test')
    def test_link_about_smtp(self):
        """
        протестировать ссылку "lets talk about smtp?"

        шаги:
            1) кликнуть ссылку "lets talk about smtp?"
            2) проверить, что url открывшейся страницы равен необходимому url

        url должен быть следующим: "https://ru.wikipedia.org/wiki/SMTP"
        """
        self.page_home.click(self.page_home.locators.LINK_ABOUT_SMTP)
        self.switch_to_last_opened_tab()
        self.check_url('https://ru.wikipedia.org/wiki/SMTP')
