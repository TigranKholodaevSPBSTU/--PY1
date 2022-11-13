import string
from random import sample
def get_random_password() -> str:
    uppercase = [up for up in string.ascii_uppercase]
    lowercase = [low for low in string.ascii_lowercase]
    numbers = [str(i) for i in range(10)]
    random_password_list = sample(uppercase + lowercase + numbers, 8)
    random_password = ''.join(random_password_list)
    return random_password

print(get_random_password())
