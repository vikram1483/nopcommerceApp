from selenium import webdriver
import pytest

# Background behind creating the conftest.py

# In the test_login.py module , we have written 2 test functions namely "test_login()" and "test_homePageTitle"
# In each of them we have repeated the following driver initiation code
    # self.driver = webdriver.Chrome()

# Going by this trend if we have say 50 test functions  then we have to include this line of code in each one of them
# which is redundant.So to avoid this if we initialise driver in separate piece of file like in a fixture()
# and make that utilisable across all the test functions then it would lead to avoiding redundancy.
# Ultimately when we call this setup() fixture , it would return the driver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser............")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser............")
    else:
        driver=webdriver.Edge()
        print("Launching Internet Explorer browser.....")

    return driver

# Running tests on the desired browsers
# Methods to get the browser from the command prompt
# pytest.addoption() method will get the value from the CLI/hooks

# Once we get the value from command line into the "--browser" variable , we have to pass that browser name to the setup()
# The setup() will decide which browser to launch
# To do this we have to create one more pytest fixture called "browser"

def pytest_addoption(parser):    # This will get the value from CLI/hooks
    parser.addoption("--browser")


# whatever browser name we have passed through command line , the pytest.addoption() method will get it.
# After getting the browser name into the "--browser" variable of the pytest_addoption(),
# the fixture() namely browser(request) will send the "--browser" variable value present in the fixture()
# to the setup()
@pytest.fixture()
def browser(request):            # This will return the Browser value to the setup()
    return request.config.getoption("--browser")

############ Pytest HTML Report #################

# It is a hook for adding environment info into HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Vikram'
    config._metadata['Browser'] = 'Chrome,Firefox'

# It is a hook for deleting/modifying environment info into HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)