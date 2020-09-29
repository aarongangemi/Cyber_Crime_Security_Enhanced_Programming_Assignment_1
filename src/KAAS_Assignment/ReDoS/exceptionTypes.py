'''
Purpose: Specify exception types for different errors that could occur
Contributors: Sho Kogota, Alex McLeod
'''
class Error(Exception):
    pass

class emailLengthException(Error):
    pass

class emailInvalidException(Error):
    pass

class usernameLengthException(Error):
    pass

class usernameInvalidException(Error):
    pass

class regexInputLengthException(Error):
    pass

class inputStringLengthException(Error):
    pass

class trimLengthException(Error):
    pass
