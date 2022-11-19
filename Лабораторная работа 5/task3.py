from random import randrange

def get_unique_list_numbers(start=-10, stop=10, size=15) -> list[int]:
    res_list = []
    if abs(start) + abs(stop) < size:
        raise ValueError('Уникальный список получить невозможно!')
    while len(res_list) < size:
        res = randrange(start, stop + 1)
        if res not in res_list:
            res_list.append(res)
    return res_list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
