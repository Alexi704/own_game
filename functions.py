import json


def read_questions():
    """Читаем файл с вопросами"""
    with open('questions.json', encoding='utf-8') as file:
        data = json.load(file)
    return data


# print(type(read_questions()), read_questions())
# print(read_questions())


def check_answer():
    """Проверяем на все вопросы мы ответили или нет"""
    data = read_questions()
    all_answer = []
    for _, price in data.items():
        for _, price_variables in price.items():
            all_answer.append(price_variables['asked'])
    if False in all_answer:
        return False
    else:
        return True


# print(check_answer())


def data_output_screen():
    """Выводим на экран категорию вопроса и цену вопроса"""
    data = read_questions()
    max_len_word_category = max(len(w) for w in list(data.keys()))  # находим длину самого длинного слова
    info_game = '\n'
    for category, category_variables in data.items():
        info_game += category.rjust(max_len_word_category)
        for price, price_variables in category_variables.items():
            if not price_variables['asked']:
                info_game += price.rjust(5)
            else:
                info_game += ''.rjust(5)
        info_game += '\n'
    return info_game[:-1]


# print(data_output_screen())


def user_selection(user_input):
    """Выбор пользователем категории и цены категории"""
    if user_input.strip().count(' ') == 1:
        user_input = user_input.strip().title().split()
        return user_input[0], int(user_input[1])
    else:
        return 'Введите категорию и цену через пробел!'


def is_question(user_category, user_price):
    """Проверка наличия выбранной категории и цены вопроса"""
    pass

