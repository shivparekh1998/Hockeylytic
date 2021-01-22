# This contains all helper functions for the project
import re
# -------------------------------------------------- USERS -------------------------------------------------------------


def find_special_chars(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(string) == None:
        return False
    elif string == '':
        return True
    else:
        return True
