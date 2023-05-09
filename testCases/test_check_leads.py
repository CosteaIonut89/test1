import pytest
from selenium import webdriver
import requests

from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common import action_chains



from selenium.webdriver.support.ui import Select
import time
import os
import glob
# import cv2
# import numpy as np

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

from Objects.objects import Boost_media,Zoho_crm
import keyword
from datetime import date
from datetime import datetime
import time

@pytest.mark.usefixtures("setup")
@pytest.hookimpl(hookwrapper=True)
class Test_Boost:
    baseURL = 'https://marketing.boostmediagroup.com/grab-your-free-marketing-assessment-test'
    first_name = 'Test'
    last_name = 'Automation'
    email = 'testautomation@boostmediagroup.com'
    user_zoho = 'george.costea@boostmediagroup.com'
    password_zoho = 'Salbutamol8!'
    baseURL2 =  'https://crm.zoho.com/crm/org20674243/tab/Leads/custom-view/634876000000012663/list'

    def test_send_lead(self):
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Boost_media(self.driver)
        self.lp_zoho = Zoho_crm(self.driver)
        self.lp.click_username()
        self.lp.set_username(self.first_name)
        self.lp.set_lastname(self.last_name)
        time.sleep(2)
        # Find element by ID or some other method
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div[4]/div[1]/div/div/input')
        # Run JavaScript to scroll until the element is in view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element);
        self.lp.set_email(self.email)
        time.sleep(2)
        self.lp.click_downloade()
        time.sleep(5)
        self.driver.get(self.baseURL2)
        time.sleep(5)
        self.lp_zoho.click_sign()
        time.sleep(2)
        self.lp_zoho.input_user(self.user_zoho)
        time.sleep(2)
        self.lp_zoho.clic_next()
        time.sleep(2)
        self.lp_zoho.input_password(self.password_zoho)
        time.sleep(2)
        self.lp_zoho.clic_next()

        time.sleep(50)