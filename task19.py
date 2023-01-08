import re


def is_password_valid(password):
    if len(password) < 8:
        return False

    pass_regexp_1 = r'.*[a-z]+.*'
    pass_regexp_2 = r'.*[A-Z]+.*'
    pass_regexp_3 = r'.*[0-9]+.*'
    pass_regexp_4 = r'.*[!@#$%^&*()_,.]+.*'

    pass_check_pattern_1 = re.compile(pass_regexp_1)
    pass_check_pattern_2 = re.compile(pass_regexp_2)
    pass_check_pattern_3 = re.compile(pass_regexp_3)
    pass_check_pattern_4 = re.compile(pass_regexp_4)

    result = bool(pass_check_pattern_1.match(password) and pass_check_pattern_2.match(password) and 
        pass_check_pattern_3.match(password) and pass_check_pattern_4.match(password))

    return result


print(is_password_valid('a'))
print(is_password_valid('12345678'))
print(is_password_valid('1aA@'))
print(is_password_valid('1aA@5678'))
print(is_password_valid('1aADDD@5678'))
print(is_password_valid(''))
