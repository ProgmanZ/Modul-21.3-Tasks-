# Задача 2. Непонятно!


def check_entered_data(user_string):

    if user_string.startswith('{') and user_string.endswith('}'):
        if ':' in user_string and len(user_string) > 5 and not user_string.endswith(':}' or '{:'):
            result = 'Dict'
            'dict'
        elif len(user_string) > 2:
            result = 'Set'
        else:
            result = 'Dict'
    elif user_string.startswith('[') and user_string.endswith(']'):
        result = 'List'
    elif user_string.startswith('(') and user_string.endswith(')'):
        result = 'Tuple'
    else:
        result = 'String'
    return result


user_enter = input('Введите данные: ')
type_data = check_entered_data(user_enter)

if type_data == 'Dict':
    print('Тип данных: dict (Словарь).\nИзменяемый (mutable).')
    if len(user_enter) == 2:
        user_enter = dict()

    else:
        user_enter = list(user_enter.strip('{}').split(','))
        temp_dict = dict()
        for data in user_enter:
            data = data.strip()
            left = data[:data.index(':')].strip('\'')
            right = data[data.index(':') + 1:].strip()
            temp_dict[left] = right
        user_enter = temp_dict

elif type_data == 'Tuple':
    user_enter = tuple(user_enter.strip('()'))
    print('Тип данных: tuple (Кортеж).\nНеизменяемый (immutable).')

elif type_data == 'List':
    user_enter = list(user_enter.strip('[]'))
    print('Тип данных: list (список)\nИзменяемый (mutable).')

elif type_data == 'Set':
    user_enter = user_enter.strip('{}')
    user_enter = set(user_enter)
    print('Тип данных: set (Сет).\nИзменяемый (mutable).')

else:
    print('Тип данных: str (Строка).\nНеизменяемый (immutable).')


print('Id объекта:', id(user_enter), type(user_enter))


