from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
@pytest.fixture()
def setup(browser):
    if browser == "IE":
        serv_obj = Service()
        driver = webdriver.Ie(service=serv_obj)

    elif browser == "firefox":
        serv_obj = Service()
        driver = webdriver.Firefox(service=serv_obj)
    else:
        serv_obj = Service()
        driver = webdriver.Chrome(service=serv_obj)
        return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")




def pytest_configure(config):
    config._metadata["project name"]="nop commerce"
    config._metadata["module name"] = "customers"
    config._metadata["Tester"] = "mukesh"

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("plugins", None)






