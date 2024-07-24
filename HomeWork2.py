# Домашнее задание по теме "Интроспекция"
# Цель задания:
#
# Закрепить знания об интроспекции в Python.
# Создать персональную функции для подробной интроспекции объекта.
#
# Задание:
# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию
# этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#    - Тип объекта.
#    - Атрибуты объекта.
#    - Методы объекта.
#    - Модуль, к которому объект принадлежит.
#    - Другие интересные свойства объекта, учитывая его тип (по желанию).
#
#
# Пример работы:
# number_info = introspection_info(42)
# print(number_info)
#
# Вывод на консоль:
{'type': 'int', 'attributes': ['__abs__', '__add__', ...], 'methods': [], 'module': '__main__'}

def introspection_info(obj):
    # Определение типа объекта
    obj_type = type(obj).__name__

    # Получение атрибутов объекта
    attributes = dir(obj)

    # Получение методов объекта
    methods = [method for method in attributes if callable(getattr(obj, method))]

    # Определение модуля, к которому объект принадлежит
    module = obj.__class__.__module__

    #  Определить, является ли определенный объект экземпляром указанного класса.
    isinstance_obj = isinstance(obj, int)

    # возвращает идентификатор указанного объекта.
    id_obj = id(obj)


    # Создание словаря с информацией об объекте
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module, 'isinstance_int': isinstance_obj, 'id': id_obj},
            # 'other_properties': other_properties}

    return info

# Интроспекция числа
number_info = introspection_info(42)
print(number_info)

# Интроспекция строки
string_info = introspection_info('Hello')
print(string_info)

#  Интроспекция списка
list_info = introspection_info([1, 20, 4.0, 'word'])
print(list_info)