# generator.py

def generate_email_tests():
    
    email_tests = [
        "test@gmail.com",      # valid
        "user@yahoo.com",      # valid
        
        "test@",               # invalid
        "@gmail.com",          # invalid
        "testgmail.com",       # missing @
        
        "",                    # empty
        "a@b.c",               # very short
        "verylongemailaddressverylongemailaddress@gmail.com"
    ]
    
    return email_tests


def generate_password_tests(min_length=8, max_length=16):

    password_tests = [
        "",                     # empty
        "123",                  # too short
        "password",             # weak
        "PASSWORD",             # uppercase only
        "12345678",             # numbers only
        "!!!!!!!!",             # symbols only
        
        "Pass123!",             # strong valid
        "a" * min_length,       # boundary min
        "b" * max_length        # boundary max
    ]

    return password_tests