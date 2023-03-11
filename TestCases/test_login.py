import pytest
from selenium import webdriver
from Utilities.CustomLogger import LogGen
from Utilities.readProperties import ReadConfig
from PageObjects.LoginPage import Loginpage

class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    useremail=ReadConfig.getUserMail()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("***** Test_001_login *****")
        self.logger.info("***** verfying homepage title *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
            self.logger.info("***** Test_001_login *****")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\"+"test_login.png")
            self.logger.error("***** home page title failed *****")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("**** verfying login test *****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=Loginpage(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***** Login test passeed *****")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
            self.logger.error("***** Login Test failed *****")
            assert False












