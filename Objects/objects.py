from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Zoho_crm:
    sing_in  ='zgh-login'
    email = 'login_id'
    next = 'nextbtn'
    password = 'password'

    def __init__(self, driver):
        self.driver = driver

    def input_password(self,password_zoho):
        self.driver.find_element_by_id(self.password).send_keys(password_zoho)

    def clic_next(self):
        self.driver.find_element_by_id(self.next).click()

    def input_user(self,user_zoho):
        self.driver.find_element_by_id(self.email).send_keys(user_zoho)

    def click_sign(self):
        self.driver.find_element_by_class_name(self.sing_in).click()




class Boost_media:

    first_name = 'elInput'
    download_button  ='//*[@id="col-left-113"]/div'
    email_field = '/html/body/div[1]/div[6]/div/div[4]/div[1]/div/div/input'


    def __init__(self, driver):
        self.driver = driver

    # Example
    def click_delete_room_group(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.delete_room_group).click()

    def set_whiteboard(self, page_title_name):
        self.driver.find_element_by_id(self.name_whiteboard).send_keys(page_title_name)

    def click_username(self):
        self.driver.find_elements_by_class_name(self.first_name)[5].click()

    def set_username(self,first_name):
        self.driver.find_elements_by_class_name(self.first_name)[5].send_keys(first_name)

    def set_lastname(self,last_name):
        self.driver.find_elements_by_class_name(self.first_name)[6].send_keys(last_name)

    def click_email(self):
        self.driver.find_element_by_xpath(self.first_name).click()

    def set_email(self,email):
        self.driver.find_element_by_xpath(self.email_field).send_keys(email)

    def click_downloade(self):
        self.driver.find_element_by_xpath(self.download_button).click()