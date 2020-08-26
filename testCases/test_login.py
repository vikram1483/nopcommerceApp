import pytest
from selenium import webdriver
# To access all the action methods from the LoginPage class we have to
# import the "LoginPage" class. The "LoginPage" class is part of the
# module "LoginPage.py". This module "LoginPage.py" is present in the
# package "pageObjects".So we have to import this package
# Syntax: "from pkg_name.module_name import class_name"

# Now to make use of the static methods in the ReadConfig class
# of the readProperties file , we have to import that class
# This is found in the utilities package
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    # Here instead of hard coding the values into the following 3 class variables
    # we are getting their values from the static methods of the "ReadConfig" class
    # present in the readProperties file

    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    # Now we will write 2 test methods in this class
    # For verifying the login functionality
    # For verifying the "Home Page Title" text
    # Here self.driver refers to the class variable "driver"

    # Here to avoid writing of driver initialization code like "self.driver=webdriver.Chrome()"
    # in each and every test method we have utilised setup() fixture and we have made the
    # test method "test_homePageTitle" receive the setup() fixture as an argument and
    # make the self.driver class variable receive that fixture like self.driver=setup
    # Here the setup() fixture will return the driver and that driver will be assigned to self.driver eventually

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("************** Test_001_Login **********")
        self.logger.info("************** Verifying Home Page Title **********")

        self.driver=setup
        self.driver.get(self.baseURL)
        actual_title=self.driver.title
        print(actual_title)
        # Here if the title matches assertion of True will happen ( Passing of test case ) and finally driver will be closed.
        # For failing the test try giving a wrong title text like "Your store. Login123" and see that a error screenshot
        # will be captured.
        if actual_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************** Home Page Title test is passed **********")
        else:
        # Here if the title doesnt match, screenshot of failure will be taken and then driver will be closed
        # and finally assertion of False will happen ( Failing the test case )
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************** Home Page Title test is failed **********")
            assert False


    # Here to avoid writing of driver initialization code like "self.driver=webdriver.Chrome()"
    # in each and every test method we have utilised setup() fixture and we have made the
    # test method "test_login" receive the setup() fixture as an argument and
    # make the self.driver class variable receive that fixture like self.driver=setup
    # Here the setup() fixture will return the driver and that driver will be assigned to self.driver eventually

    # Normal login comes under both sanity and regression
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("************** Verifying Login Page Title **********")

        # Here self.driver refers to the class variable "driver"
        self.driver=setup

        # Since all the variables used here like "username","password"
        # and "baseURL" are class variables they have to be referenced
        # like "self.class_variable_name"

        self.driver.get(self.baseURL)
        # Here to access the action methods of the LoginPage class
        # we have to create object of that class and access through it.
        # Here since object "lp" is used in this class we have to
        # refer it using self as always

        # Now whenever we call the LoginPage class , the constructor
        # of it ( i.e LoginPage class) which is "__init__(self,driver)"
        # will be automatically invoked.
        # But this constructor is expecting a driver as a parameter
        # and so we will pass "self.driver" as parameter

        self.lp=LoginPage(self.driver)

        # Now after creating the object of the "LoginPage" class
        # we can invoke the action methods present in that class
        # using the convention "self.lp.action_method_name"
        # Since all the variables used here like "username","password"
        # and "baseURL" are class variables they have to be referenced
        # like "self.class_variable_name"

        self.lp.setUserName(self.username)

        self.lp.setPassword(self.password)

        self.lp.clickLogin()

        act_title = self.driver.title
        print(act_title)

        # Now we have to validate the successful login in the Login Page
        # Here if the title matches assertion of True will happen ( Passing of test case ) and finally driver will be closed.
        # For failing the test try giving a wrong title text like "Dashboard / nopCommerce administration123"
        # and see that a error screenshot will be captured.

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************** Login test passed **********")
            self.driver.close()

        else:
            # Here if the title doesnt match, screenshot of failure will be taken and then driver will be closed
            # and finally assertion of False will happen ( Failing the test case )
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************** Login test failed **********")
            assert False
