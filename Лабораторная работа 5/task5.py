import string
from random import sample
def get_random_password() -> str:
    length = 8
    random_password_list = sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, length)
    random_password = ''.join(random_password_list)
    return random_password

print(get_random_password())
