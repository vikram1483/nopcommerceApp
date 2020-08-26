class LoginPage:
    # We have to capture locators of each and every web element in the Login Page
    # URL of the Login Page is "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # The web elements in the login page are "Email" , "Password" , "LOG IN".
    # After logging into the homepage "https://admin-demo.nopcommerce.com/admin/"
    # the web element to logout is "Logout".
    # So totally the locators of the 4 web elements namely "Email","Password","LOG IN" and "Logout" have to be captured.

    # Here we will follow a naming convention for the web element holding variable like
    #  "webelementtype_inputholder_locatortype" and example of it will be like "textbox_username_id"
    # Here web element type can be an textbox/dropdown/radio/checkbox/button/link etc
    # input holder can be username,password,login,logout value asker
    # The locator types can be id,tag_name,class_name,xpath,css_selector,link_text and partial_link_text

    # Captured Locators for all the web elements
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//input[@class='button-1 login-button']"
    link_logout_linktext="Logout"

    # Initialising the class variable "driver"  automatically whenever an object of Login Page class is created
    # This is done through the Login page constructor which is "__init__(self)"
    # The driver in the constructor argument will come through the test case
    # The constructor will capture the driver coming as argument from the test case and that test case driver
    # will be used to initialise the Login Page class variable "driver" like (self.class_variable=argument value)
    # Finally this "self.driver" will be used in writing the action methods for all the webelements mentioned above
    def __init__(self,driver):
        self.driver=driver

    # Finally this "self.driver" will be used in writing the action methods for all the webelements locators mentioned above
    # Now writing the action methods for all the web elements mentioned like "username","password","login" and "logout"
    # Action Methods pertain to --> entering the "username" , entering the "password" , "clicking the "login" button
    # and clicking the "logout" button.
    # These action methods will be called later from the test cases

    # Here the "username" parameter will be used to set the value of the "username" web element
    # Here the variables which have captured the web element locators belong to the class
    # So they have to accessed like "self.class_variable_names"
    # Before entering the values plz clear the textbox so that no traces of previous input will be there
    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    # Here the "password" parameter will be used to set the value of the "password" web element
    # Here the variables which have captured the web element locators belong to the class
    # So they have to accessed like "self.class_variable_names"
    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()










