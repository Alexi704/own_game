import json


def read_questions():
    """Читаем файл с вопросами"""
    with open('questions.json', encoding='utf-8') as file:
        data = json.load(file)
    return data


# print(type(read_questions()), read_questions())
# print(read_questions())


def data_output_screen():
    """Выводим на экран категорию вопроса и цену вопроса"""
    data = read_questions()
    max_len_word_category = max(len(w) for w in list(data.keys()))  # находим длину самого длинного слова
    info_game = ''
    for category, category_variables in data.items():
        info_game += category.rjust(max_len_word_category)
        for price, price_variables in category_variables.items():
            if not price_variables['asked']:
                info_game += price.rjust(5)
            else:
                info_game += ''.rjust(5)
        info_game += '\n'
    return info_game
# print(data_output_screen())
