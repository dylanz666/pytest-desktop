from pages.base_page import BasePage
from tools.decorators import allure_step, screenshot_on_failure


class HomePage(BasePage):
    def __init__(self, application):
        self.application = application
        self.window = None
        self.window_title = ""

        super().__init__(self.application)

    @allure_step
    @screenshot_on_failure
    def is_opened(self):
        self.window = self.application.window()
        self.window_title = self.window.window_text()
        assert "- Notepad" in self.window_title, "The notepad is not opened"

    @allure_step
    @screenshot_on_failure
    def clear_document(self):
        self.application[self.window_title].type_keys('^a')
        self.application[self.window_title].type_keys('{DEL}')
        self.window_title = self.window.window_text()

        assert self.application[self.window_title].Document.texts() == ['']

    @allure_step
    @screenshot_on_failure
    def input_text_to_document(self, text):
        self.application[self.window_title].Document.type_keys(text, with_spaces=True, pause=0.1)

        self.window_title = self.window.window_text()

    @allure_step
    @screenshot_on_failure
    def get_value_of_document(self):
        return self.application[self.window_title].Document.texts()

    @allure_step
    @screenshot_on_failure
    def close(self):
        return self.window.close()
