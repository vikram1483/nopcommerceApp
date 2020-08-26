import time

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
from utilities import XLUtils

class Test_002_DDT_Login:
    # Here instead of hard coding the values into the following 3 class variables
    # we are getting their values from the static methods of the "ReadConfig" class
    # present in the readProperties file

    baseURL=ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    logger=LogGen.loggen()

    # Here to avoid writing of driver initialization code like "self.driver=webdriver.Chrome()"
    # in each and every test method we have utilised setup() fixture and we have made the
    # test method "test_login" receive the setup() fixture as an argument and
    # make the self.driver class variable receive that fixture like self.driver=setup
    # Here the setup() fixture will return the driver and that driver will be assigned to self.driver eventually

    @pytest.mark.regression   # DDT comes under regression
    def test_login_DDT(self,setup):
        self.logger.info("************** Test_002_DDT_Login **********")
        self.logger.info("************** Verifying Login DDT test **********")
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

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in excel are ",self.rows)

        lst_status=[]   # Empty list variable

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)


            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    lst_status.append("Pass")

                elif self.exp=="Fail":
                    self.logger.info("** Failed ***")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")

                elif self.exp=="Fail":
                    self.logger.info("*** Passed***")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("***  Login DDT test passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info(("*** Login DDT test failed ***"))
            self.driver.close()
            assert False

        self.logger.info("***** End of Login DDT Test ********")
        self.logger.info("********** Completed  TC_LoginDDT_002")