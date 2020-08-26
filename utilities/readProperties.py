# readProperties.py --> A utilties file to read the contents of the "config.ini" file.
# In Python we have a special in built package called "confidgparser" to read the conetents from a "config.ini" file.
# So we will import that module into our "readProperties.py" file.

#import configparser

# There is a class called "RawConfigParser" inside the configparser package.
# We need to create an object of class "RawConfigParser()"

#config = configparser.RawConfigParser()

# Then we use the read() of the "RawConfigParser()" class to load the "config.ini" file
# We need to provide the location of the "config.ini" as an argument to read()

#config.read(".\\Configurations\\config.ini")


# Reading the contents of the "config.ini"
# We will create a class with 3 static methods to access the 3 variables defined in the config.ini file.
# Here for each variable in the config.ini file we will create 1 corresponding static method like a page object class

# class ReadConfig:
#     @staticmethod
#     def getApplicationURL():
        # Here for get() we have to pass 2 arguments where first arg refers to the
        # category name in the config.ini file and the second arg refers to the variable
        # We want to make this getApplicationURL() as a static method so that
        # it can be accessed by the class directly instead of through object.
        # So we will put a "@staticmethod" decorator around the method and
        # remove the default argument "self" as its not used for a static method
        # Finally from the actual test case this static method will be called and
        # the values are returned accordingly.

        # url=config.get('required data','baseURL')
        # return url

    # @staticmethod
    # def getUseremail():
    #     username = config.get('required data', 'useremail')
    #     return username
    #
    # @staticmethod
    # def getPassword():
    #     password = config.get('required data', 'password')
    #     return password


from configparser import ConfigParser
parser=ConfigParser()
#parser.read(".\\Configurations\\config.ini")
parser.read("C:\\Users\\vikram1483\\PycharmProjects\\nopcommerceApp\\Configurations\\config.ini")

print(parser.get('required data','baseURL'))
print(parser.get('required data','useremail'))
print(parser.get('required data','password'))

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=parser.get('required data','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = parser.get('required data', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = parser.get('required data', 'password')
        return password
