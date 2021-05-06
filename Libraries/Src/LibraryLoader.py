import Browser
from Browser import SupportedBrowsers

class LibraryLoader:
    """
    https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
    """
    __instance = None

    def __init__(self):
        if self.__class__.__instance is not None:
            raise Exception(f'{self.__class__} is a singleton. Use get_instance() instead')
        self.__class__.__instance = self
        self._bl = None  # lazy initialization

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls()
        return cls.__instance

    @property
    def bl(self):
        if self._bl is None:
            self.bl = Browser.Browser(timeout='30s', auto_closing_level='SUITE', enable_presenter_mode=True)
            self._bl.new_browser(browser=SupportedBrowsers.chromium, headless=False)
            self._bl.new_context()
            self._bl.new_page()
        return self._bl

    @bl.setter
    def bl(self, bl):
        self._bl = bl

    def __del__(self):
        self._bl.close_browser(browser='ALL')