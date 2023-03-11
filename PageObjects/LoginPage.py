from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
class Loginpage:
    textbox_username_XPATH="//*[@id='Email']"
    textbox_password_ID="Password"
    button_login_XPATH="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_LINK_TEXT="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_XPATH).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_XPATH).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_ID).clear()
        self.driver.find_element(By.ID,self.textbox_password_ID).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_XPATH).click()

    def clickLogout(self):
        self.driver.find_element_(By.LINK_TEXT,self.link_logout_LINK_TEXT).click()
