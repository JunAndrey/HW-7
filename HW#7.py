import os
from pprint import pprint

log_file_name = "HW#7.txt"
base_path = os.getcwd()
full_path = os.path.join(base_path, log_file_name)

cook_book = {}
def file_reader(file_path):
    with open(file_path, encoding="utf-8") as file:
        is_dish_name = 1
        for line in file:
            ln = line.strip()
            if is_dish_name == 1 and ln != '':
                cook_book[ln] = []
                dish = ln
                is_dish_name = 0
                file.readline() # Пропуск строки с колчеством блюд
            elif is_dish_name == 0 and ln == '':
                is_dish_name = 1
            else:
                line_split = ln.split(" | ")
                cook_book[dish].append({})
                cook_book[dish][-1]['ingredient_name'] = line_split[0]
                cook_book[dish][-1]['quantity'] = int(line_split[1])
                cook_book[dish][-1]['measure'] = line_split[2]

        pprint(cook_book, indent=1, width=100)

# file_reader(full_path)

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for some_dish in dishes:
        if some_dish in cook_book.keys():
            for key in cook_book[some_dish]:
                if key['ingredient_name'] not in result.keys():
                    result[key['ingredient_name']] = {}
                    dict = result[key['ingredient_name']]
                    dict['measure'] = key['measure']
                    dict['quantity'] = key['quantity'] * person_count
                else:
                    result[key['ingredient_name']]['quantity'] += key['quantity'] * person_count
        else:
            print('Выберите корректное название блюда')
            return
    pprint(result)
# get_shop_list_by_dishes(['Фахитос', 'Утка по-пекински', 'Омлет'], 1)

file_name = ["1.txt", "2.txt", "3.txt"]
def init_file(file_name):
    dict1 ={}
    for name in file_name:
        with open(name, encoding="utf-8") as file_1:
            dict1[name] = len(file_1.readlines())
            sorted_values = sorted(dict1.values())
            sorted_dict = {}
    for i in sorted_values:
        for k in dict1.keys():
            if dict1[k] == i:
                sorted_dict[k] = dict1[k]
                break
    print(sorted_dict)
    with open("file.txt", 'w', encoding='utf-8') as document:
        for key in sorted_dict.keys():
            document.write(key + '\n')
            document.write(str(sorted_dict[key]) + '\n')
            with open(key, 'r', encoding='utf-8') as read_doc:
                for line in read_doc:
                    document.write(line.strip() + '\n')

init_file(file_name)

