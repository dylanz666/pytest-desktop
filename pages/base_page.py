import time

from pywinauto import timings

from tools.decorators import allure_step


class BasePage:
    def __init__(self, application):
        self.application = application

    @allure_step
    def input_text(self, window_title, control_type, text):
        """在指定窗口的指定控件中输入文本"""
        window = self.application.window(title=window_title)
        window.child_window(control_type=control_type).type_keys(text, with_spaces=True)

    @allure_step
    def click_button(self, window_title, button_text):
        """点击指定窗口中的按钮"""
        window = self.application.window(title=window_title)
        window.child_window(title=button_text, control_type="Button").click()

    @allure_step
    def select_menu(self, window_title, menu_path):
        """选择指定窗口中的菜单项"""
        window = self.application.window(title=window_title)
        window.menu_select(menu_path)

    @allure_step
    def save_file(self, window_title, filename):
        """保存文件"""
        self.select_menu(window_title, "File->Save As")
        time.sleep(1)  # 等待保存对话框出现
        save_dialog = self.application.SaveAs
        save_dialog.Edit.set_text(filename)
        save_dialog.Save.click()
        time.sleep(2)  # 等待保存完成

    @allure_step
    def close_application(self, window_title):
        """关闭指定的应用程序"""
        window = self.application.window(title=window_title)
        window.close()
        if window.is_open():
            window.DontSave.click()

    @allure_step
    def select_dropdown(self, window_title, dropdown_title, item_text):
        """选择指定窗口中的下拉菜单项"""
        window = self.application.window(title=window_title)
        dropdown = window.child_window(title=dropdown_title, control_type="ComboBox")
        dropdown.select(item_text)

    @allure_step
    def get_control_text(self, window_title, control_type):
        """获取指定控件的文本"""
        window = self.application.window(title=window_title)
        return window.child_window(control_type=control_type).window_text()

    @allure_step
    def wait_for_control(self, window_title, control_type, timeout=10):
        """等待指定控件可用"""
        window = self.application.window(title=window_title)
        timings.wait_until_passes(timeout, 0.5, lambda: window.child_window(control_type=control_type).exists())

    @allure_step
    def input_password(self, window_title, control_type, password):
        """在指定控件中输入密码"""
        self.input_text(window_title, control_type, password)

    @allure_step
    def send_shortcut(self, window_title, shortcut):
        """发送键盘快捷键"""
        window = self.application.window(title=window_title)
        window.type_keys(shortcut, with_spaces=True)

    @allure_step
    def get_window_title(self):
        """获取当前窗口的标题"""
        window = self.application.window()
        title = window.window_text()
        print(f"Current window title: {title}")
        return title
