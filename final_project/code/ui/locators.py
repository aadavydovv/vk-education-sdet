from selenium.webdriver.common.by import By


def link_by_title(title):
    return By.XPATH, f'//a[text()="{title}"]'


def home_page_central_link_by_title(title):
    return By.XPATH, f'//div[text()="{title}"]/..//a'


def menu_by_title(title):
    return By.XPATH, f'//ul[@class="uk-navbar-nav uk-hidden-small"]/li/a[contains(text(), "{title}")]'


def menu_element_by_title(title_menu, title_element):
    menu = menu_by_title(title_menu)
    return menu[0], f'{menu[1]}/../div//a[contains(text(), "{title_element}")]'


class LocatorsBase:

    INPUT_USERNAME = (By.ID, 'username')
    INPUT_PASSWORD = (By.ID, 'password')
    BUTTON_SUBMIT = (By.ID, 'submit')
    TEXT_ERROR = (By.ID, 'flash')


class LocatorsLogin(LocatorsBase):

    LINK_CREATE_ACCOUNT = link_by_title('Create an account')


class LocatorsRegistration(LocatorsBase):

    INPUT_EMAIL = (By.ID, 'email')
    INPUT_PASSWORD_CONFIRM = (By.ID, 'confirm')
    CHECKBOX_TERM = (By.ID, 'term')
    LINK_LOGIN = link_by_title('Log in')


class LocatorsHome(LocatorsBase):

    BUTTON_LOGOUT = (By.ID, 'logout')
    TEXT_LOGIN_NAME = (By.ID, 'login-name')

    LINK_HOME = link_by_title('HOME')

    _MENU_PYTHON_TITLE = 'Python'
    MENU_PYTHON = menu_by_title(_MENU_PYTHON_TITLE)
    LINK_PYTHON_HISTORY = menu_element_by_title(_MENU_PYTHON_TITLE, 'Python history')
    LINK_ABOUT_FLASK = menu_element_by_title(_MENU_PYTHON_TITLE, 'About Flask')

    _MENU_LINUX_TITLE = 'Linux'
    MENU_LINUX = menu_by_title(_MENU_LINUX_TITLE)
    LINK_DOWNLOAD_CENTOS = menu_element_by_title(_MENU_LINUX_TITLE, 'Download Centos7')

    _MENU_NETWORK_TITLE = 'Network'
    MENU_NETWORK = menu_by_title(_MENU_NETWORK_TITLE)
    LINK_WIRESHARK_NEWS = menu_element_by_title(_MENU_NETWORK_TITLE, 'News')
    LINK_WIRESHARK_DOWNLOAD = menu_element_by_title(_MENU_NETWORK_TITLE, 'Download')
    LINK_TCPDUMP_EXAMPLES = menu_element_by_title(_MENU_NETWORK_TITLE, 'Examples')

    LINK_WHAT_IS_API = home_page_central_link_by_title('What is an API?')
    LINK_FUTURE_OF_INTERNET = home_page_central_link_by_title('Future of internet')
    LINK_ABOUT_SMTP = home_page_central_link_by_title('Lets talk about SMTP?')

    TEXT_FACT = (By.XPATH, "//footer/div/p[2][text()]")
