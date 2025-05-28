import os
import time

import pytest
import allure
from pywinauto import Application

from constants.severity import Severity
from pages.home_page import HomePage
from tools.config_util import ConfigUtil


@allure.feature("Feature: input content to notepad")
class TestDesktopDemo:
    def setup_class(self):
        os.system("taskkill /IM notepad.exe /F")

        self.application_path = ConfigUtil.get_application_path()
        Application().start('notepad.exe')
        self.application = Application(backend="uia").connect(path=self.application_path, title="*- Notepad")

        self.home_page = HomePage(self.application)

    def teardown_class(self):
        self.home_page.close()

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    @pytest.mark.P0
    @pytest.mark.sanity
    @allure.severity(Severity.BLOCKER.value)
    @allure.title("Notepad: input valid text")
    @allure.description("Notepad: input valid text")
    @allure.testcase("https://www.baidu.com")
    # @pytest.mark.skip
    def test_input_valid_text_to_notepad(self):
        expected_text = "Hello World!"

        self.home_page.is_opened()
        self.home_page.clear_document()

        self.home_page.input_text_to_document(expected_text)
        actual_text = self.home_page.get_value_of_document()
        assert expected_text in actual_text
