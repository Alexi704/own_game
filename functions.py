import json


def read_questions():
    """Читаем файл с вопросами"""
    with open('questions.json', encoding='utf-8') as file:
        data = json.load(file)
    return data


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


def user_selection(user_input):
    """Выбор пользователем категории и цены категории"""
    count_spaces = user_input.strip().count(' ')
    if count_spaces > 1:
        return False
    elif count_spaces == 1:
        user_input = user_input.strip().title().split()
        price = user_input[1]
        if price.isdigit():
            price = int(price)
            return user_input[0], price


def is_question(user_category, user_price):
    """Проверка наличия выбранной категории и цены вопроса"""
    data = read_questions()
    all_category = list(data.keys())
    if user_category not in all_category:
        print(f"Категории: {user_category} не существует!")
        return False

    for category, category_variables in data.items():
        if str(user_price) not in list(category_variables.keys()):
            print(f"Такой цены: \"{user_price}\" не существует!")
            return False
        elif user_category == category:
            for price, price_variables in category_variables.items():
                if user_price == int(price) and price_variables['asked'] is False:
                    return f'Слово \"{price_variables["question"]}\" в переводе означает: '
                elif user_price == int(price) and price_variables['asked'] is True:
                    print(f'Вы уже использовали данное задание.')
                    return False


# print(is_question('Еда', 100))
TOTAL_SCORE = 0
correct_answer = 0
incorrect_answer = 0


def checking_user_answer(user_answer, user_category, user_price):
    """Проверяем ответ пользователя и записываем результаты в файл"""
    global TOTAL_SCORE
    global correct_answer
    global incorrect_answer
    data = read_questions()
    for category, category_variables in data.items():
        if category == user_category:
            for price, price_variables in category_variables.items():
                if price == str(user_price):
                    price_variables["asked"] = True
                    if user_answer.strip().lower() == price_variables['answer']:
                        TOTAL_SCORE += int(price)
                        correct_answer += 1
                        result = f'Верно, +{price}. Ваш счет = {TOTAL_SCORE}'
                    else:
                        TOTAL_SCORE -= int(price)
                        incorrect_answer += 1
                        result = f'Неверно, на самом деле \"{price_variables["answer"]}\". –{price}. Ваш счет = {TOTAL_SCORE}'
    raw_json = json.dumps(data, ensure_ascii=False, indent=4)
    with open('questions.json', 'w', encoding='utf-8') as file:
        file.write(raw_json)

    total_score = {"points": TOTAL_SCORE, 'correct': correct_answer, 'incorrect': incorrect_answer}
    result_game_json = json.dumps(total_score, ensure_ascii=False, indent=4)
    with open('result_games.json', 'w', encoding='utf-8') as file:
        file.write(result_game_json)

    return result


def game_total_score():
    """Считываем файл с результатами игры"""
    with open('result_games.json', encoding='utf-8') as file:
        data = json.load(file)
        points = data['points']
        correct = data['correct']
        incorrect = data['incorrect']
    return f"""
        У нас закончились вопросы!
        Вас счет: {points}
        Верных ответов: {correct}
        Неверных ответов: {incorrect}
        """


# print(checking_user_answer('Акула', 'Животные', 200))
