import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Config.config_reader import read_config
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def setup(request):
    # Read base URL from config
    CHROMEDRIVER_VERSION = "131.0.6778.205"
    path =ChromeDriverManager(driver_version=CHROMEDRIVER_VERSION).install()
    base_url = read_config("URL", "base_url")
    chrome_options=Options
    service=Service(path)
    driver=webdriver.Chrome(service=service,options=chrome_options)

    driver.get(base_url)


    # Attach driver to the test class
    request.cls.driver = driver

    # Yield to run tests
    yield

    # Quit the driver after tests complete
    # last commit
    driver.quit()
