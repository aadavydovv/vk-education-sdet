from ui_android.locators import LocatorsSettingsAbout
from ui_android.pages.base import PageBase


class PageSettingsAbout(PageBase):
    locators = LocatorsSettingsAbout()

    def __init__(self, driver, apk_path):
        super().__init__(driver)
        self.version_apk = apk_path.stem.partition('_v')[2]

    def check_versions(self):
        version_app = self.find(self.locators.TEXT_VERSION).get_attribute('text').replace('Версия ', '')
        assert self.version_apk == version_app, f'version from apk ({self.version_apk})' \
                                                f' and version in app ({version_app}) do not match'

    def check_trademark(self):
        copyright = self.find(self.locators.TEXT_COPYRIGHT).get_attribute('text')
        assert 'Все права защищены' in copyright, 'copyright does not contain a trademark'
