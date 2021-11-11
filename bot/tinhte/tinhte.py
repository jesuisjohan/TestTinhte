import time

import tinhte.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Tinhte(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Tinhte, self).__init__()
        self.implicitly_wait(const.WAIT_TIME)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def login(self, text, password):
        self.click_burger_menu()

        login_account_option = self.find_element_by_css_selector(
            'li[class=jsx-3867722346]'
        )
        login_account_option.click()

        text_field = self.find_element_by_id('ctrl_pageLogin_login2')
        text_field.clear()
        text_field.send_keys(text)

        password_field = self.find_element_by_id('ctrl_pageLogin_password2')
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.find_element_by_xpath(
            "/html[@id='XenForo']/body/div[@class='js-uix_panels uix_panels']/div[@class='mainPanelWrapper']/div["
            "@id='uix_wrapper']/div[@id='headerMover']/div[@id='content']/div[@class='pageWidth']/div["
            "@class='pageContent']/div[@class='mainContainer_noSidebar']/div[@class='mainContent']/form["
            "@class='TinhteMods_Form']/div[@class='TinhteMods_Form_Wrapper']/input[@class='button primary'] "
        )
        login_button.click()

    '''
    change account password
    require login
    '''
    def change_password(self, current_password, new_password,
                        fill_current_password=True,
                        fill_new_password=True,
                        fill_confirm_password=True,
                        expected_to_have_error=False,
                        fill_wrong_confirm_password=False):
        self.implicitly_wait(const.WAIT_TIME)
        self.click_burger_menu()
        menu_options = self.find_elements_by_css_selector(
            'li[class="jsx-2317212796 item"]'
        )
        change_password_button = menu_options[5]
        change_password_button.click()
        self.implicitly_wait(const.WAIT_TIME)

        if fill_current_password:
            current_password_field = self.find_element_by_id('ctrl_password_original')
            current_password_field.clear()
            current_password_field.send_keys(current_password)

        if fill_new_password:
            new_password_field = self.find_element_by_id('ctrl_password')
            new_password_field.clear()
            new_password_field.send_keys(new_password)

        if fill_confirm_password:
            confirm_password_field = self.find_element_by_id('ctrl_password_confirm')
            confirm_password_field.clear()

            if fill_wrong_confirm_password:
                wrong_confirm_password = new_password + "1"
                confirm_password_field.send_keys(wrong_confirm_password)
            else:
                confirm_password_field.send_keys(new_password)

        save_change_button = self.find_element_by_xpath(
            "/html[@id='XenForo']/body/div[@class='js-uix_panels uix_panels']/div[@class='mainPanelWrapper']/div["
            "@id='uix_wrapper']/div[@id='headerMover']/div[@id='content']/div[@class='pageWidth']/div["
            "@class='pageContent']/div[@class='mainContainer_noSidebar']/div[@class='mainContent']/div["
            "@class='container']/div[@class='mainContentBlock section sectionMain insideSidebar']/form["
            "@class='xenForm AutoValidator ContactDetailsForm']/dl[@class='ctrlUnit submitUnit']/dd/input["
            "@class='button primary'] "
        )
        save_change_button.click()

        self.implicitly_wait(5)
        error_popup = self.find_elements_by_css_selector(
            'div[class="errorOverlay"]'
        )

        has_error_popup = (len(error_popup) != 0)

        if has_error_popup == expected_to_have_error:
            print("Testcase Passed!")
        else:
            print("Testcase Failed!")

    '''
    create new article on tinhte.vn homepage
    require login
    '''
    def create_new_article(self,
                           fill_text=True,
                           insert_link=True,
                           upload_image=True,
                           upload_many_images=True,):
        #self.land_first_page()
        self.implicitly_wait(const.WAIT_TIME)
        create_new_article_button = self.find_element_by_css_selector(
            'button[class="jsx-659482973 blue-switch header-mode"]'
        )
        create_new_article_button.click()

        if fill_text:
            self.fill_text()

        if insert_link:
            self.insert_link()

        if upload_image or upload_many_images:
            self.upload_one_image()

            if upload_many_images:
                self.upload_many_images()

        time.sleep(5)

        post_article_button = self.find_element_by_xpath(
            '//button[normalize-space()="Đăng Bài"]'
        )
        post_article_button.click()

    '''
    create new Fact (Facebook Story bootleg) on tinhte.vn homepage
    require login
    '''
    def create_new_fact(self,
                        fill_text=True,
                        upload_image=True,
                        upload_many_images=True):

        # self.land_first_page()
        self.implicitly_wait(const.WAIT_TIME)
        create_new_article_button = self.find_element_by_css_selector(
            'button[class="jsx-659482973 blue-switch header-mode"]'
        )
        create_new_article_button.click()

        # Switch to posting new Fact (Facebook Story bootleg) instead of article
        self.click_switch_toggle_article_and_fact()

        if fill_text:
            self.fill_text()

        if upload_image or upload_many_images:
            self.upload_one_image()

            if upload_many_images:
                self.upload_many_images()

        time.sleep(5)
        post_article_button = self.find_element_by_xpath(
            "//button[contains(.,'Đăng Bài')]"
        )
        post_article_button.click()

#region supportMethods

    def click_burger_menu(self):
        burger_menu = self.find_element_by_css_selector(
            'button[class="jsx-3867722346 burger-menu"]'
        )
        burger_menu.click()

    def fill_text(self):
        text_part = self.find_element_by_css_selector(
            'textarea[placeholder*="Viết nội dung bạn muốn chia sẻ vô đây nè"]'
        )
        text_part.clear()
        text_part.send_keys("Game God of War 2018 sắp được tải về từ Steam rồi!!")

    def insert_link(self):
        insert_link_button = self.find_element_by_css_selector(
            'button[class="jsx-659482973 thread-background-switch link-sharing"]'
        )
        insert_link_button.click()

        text_inputs = self.find_elements_by_xpath("//input[@value='']")
        link_input = text_inputs[1]
        link_input.clear()
        link_input.send_keys("https://store.steampowered.com/app/1593500/God_of_War/")

    def upload_one_image(self):
        self.find_element_by_xpath("//input[@type='file']").send_keys("D://Images/forest.jpg")

    def upload_many_images(self):
        self.find_element_by_xpath("//input[@type='file']").send_keys("D://Images/forest2.jpg")
        self.find_element_by_xpath("//input[@type='file']").send_keys("D://Images/forest3.jpg")
        self.find_element_by_xpath("//input[@type='file']").send_keys("D://Images/forest4.jpg")

    def click_switch_toggle_article_and_fact(self):
        switch = self.find_element_by_css_selector(
            'div[class*="jsx-1525902178 switch-toggle"]'
        )
        switch.click()

#endregion