# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from Config.config_reader import read_config
# from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(scope="class")
# def setup(request):
#     # Read base URL from config
#     CHROMEDRIVER_VERSION = "131.0.6778.205"
#     driver = webdriver.Chrome(
#         ChromeDriverManager(driver_version=CHROMEDRIVER_VERSION).install()
#     )
#     base_url = read_config("URL", "base_url")
#     driver = webdriver.Chrome()

#     driver.get(base_url)

#     # Attach driver to the test class
#     request.cls.driver = driver

#     # Yield to run tests
#     yield

#     # Quit the driver after tests complete
#     # last commit
#     driver.quit()
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Config.config_reader import read_config
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start browser maximized
    chrome_options.add_argument("--disable-extensions")  # Disable extensions
    chrome_options.add_argument("--disable-gpu")  # Disable GPU for headless
    chrome_options.add_argument("--no-sandbox")  # For Linux environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues

    # Read base URL from the configuration file
    base_url = read_config("URL", "base_url")

    # Initialize the Chrome driver with specified options and version
    CHROMEDRIVER_VERSION = "131.0.6778.205"
    driver = webdriver.Chrome(ChromeDriverManager(driver_version=CHROMEDRIVER_VERSION).install(),
        options=chrome_options
    )

    # Open the base URL
    driver.get(base_url)

    # Attach driver to the test class for use in tests
    request.cls.driver = driver

    # Yield to allow test execution
    yield

    # Clean up and quit the driver after tests complete
    driver.quit()
