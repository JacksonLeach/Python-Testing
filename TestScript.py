import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import customFunctions

testData = {'email':'jleach+00001@videomaker.com', 'user':'jleach00001', 'passw':'password'}


class videomakerTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.doublePasswordInput = [self.driver.find_element(By.ID, 'edit-pass-pass1'), self.driver.find_element(By.ID, 'edit-pass-passw')]
    def test_createAccount(self):
        driver = self.driver
        driver.get('http://www.videomaker.com/user/register')
        emailInput = driver.find_element(By.ID, 'edit-mail--2')
        emailInput.send_keys('jleach+00001@videomaker.com')
        usernameInput = driver.find_element(By.ID, 'edit-name--2')
        usernameInput.send_keys(testingData['user'])
        for i in self.doublePasswordInput:
            i.send_keys(testingData['passw'])
        button = driver.find_element(By.ID, 'edit-submit--4')
        ActionChains(driver).click(button).perform()
        print('User creation successful')
    def test_editProfile():
        driver = self.driver
        driver.get('http://www.videomaker.com/user')
        if ('Log in' in driver.title):
            userName = driver.find_element(By.ID, 'edit-name')
            userName.send_keys(testingData['user'])
            password = driver.find_element(By.ID, 'edit-pass')
            password.send_keys(testingData['passw'])
            button = driver.find_element(By.ID, 'edit-submit')
            ActionChains(driver).click(button).perform()
        editButton = driver.find_element(By.LINK_TEXT, 'Edit')
        ActionChains(driver).click(editButton).perform()
        editName = driver.find_element(By.ID, 'edit-name')
        editName.send_keys('jleach00002')
        submitButton = driver.find_element(By.ID, 'edit-submit')
        ActionChains(driver).click(submitButton).perform()
        editName.send_keys(testData['user'])
        for i in self.doublePasswordInput:
            i.send_keys(testData['passw'] + '1')
        ActionChains(driver).click(submitButton).perform()
        for i in self.doublePasswordInput:
            i.send_keys(testData['passw'])
        ActionChains(driver).click(submitButton).perform()
    def test_newsletterSignUp(self):
        driver = self.driver
        driver.get('http://www.videomaker.com/user')
        
    def tearDown(self):
        self.driver.close()
editProfile()
