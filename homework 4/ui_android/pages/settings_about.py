from ui_android.locators import LocatorsSettingsAbout
from ui_android.pages.base import PageBase


class PageSettingsAbout(PageBase):
    locators = LocatorsSettingsAbout()

    @staticmethod
    def _get_apk_version_from_path(apk_path):
        path_separator = None

        # тему кроссплатформенности не стал раскрывать из-за того, что не имею возможности протестить прогу на винде :(
        if '/' in apk_path:
            path_separator = '/'

        if path_separator:
            apk_name = apk_path.rpartition(path_separator)[2]
        else:
            apk_name = apk_path

        return apk_name.partition('_v')[2][:-4]

    def __init__(self, driver, config):
        super().__init__(driver)
        self.version_apk = self._get_apk_version_from_path(config['apk_path'])

    def check_versions(self):
        version_app = self.find(self.locators.TEXT_VERSION).get_attribute('text').replace('Версия ', '')
        assert self.version_apk == version_app, f'version from apk ({self.version_apk})' \
                                                f' and version in app ({version_app}) do not match'

    def check_trademark(self):
        copyright = self.find(self.locators.TEXT_COPYRIGHT).get_attribute('text')
        assert 'Все права защищены' in copyright, 'copyright does not contain a trademark'
