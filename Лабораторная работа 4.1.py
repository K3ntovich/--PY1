import collections
def get_count_char(str_):
    str_ = str_.lower()
    count = collections.Counter()
    for char in list(str_):
        if char.isalpha():
            count[char] += 1
    return dict(count)

main_str = """Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    
"""

print(get_count_char(main_str))


def toPercent(collection):
    count = 0
    for i in collection:
        count += collection[i]
    for i in collection:
        collection[i] *=100 / count
    print(collection)