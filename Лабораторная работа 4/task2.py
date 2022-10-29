def get_count_char(str_):
    dict_letter_count = {}
    str_ = str_.lower()
    for symbol in str_:
        if symbol.isalpha():
            dict_letter_count[symbol] = dict_letter_count.get(symbol, 0) + 1
    return dict_letter_count

def get_per_cent_letters(dict_):
    sum_ = sum(list(dict_.values()))
    for letter in dict_:
        dict_[letter] = round(dict_[letter] / sum_ * 100, 3)
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
dict_letters_count = get_count_char(main_str)
new_dict = get_per_cent_letters(dict_letters_count)

print(round(sum(list(new_dict.values()))))