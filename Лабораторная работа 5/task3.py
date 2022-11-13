from random import randrange

def get_unique_list_numbers() -> list[int]:
    res_list = []
    while len(res_list) < 15:
        res = randrange(-10, 11)
        if res not in res_list:
            res_list.append(res)
    return res_list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
