from functions import data_output_screen, user_selection, is_question, checking_user_answer, check_answer

if __name__ == '__main__':

    while check_answer() is False:
        print(data_output_screen())  # выводим на экран наши темы и цены
        user_input = input('Выбирайте категорию вопроса и цену:\n')

        if user_selection(user_input) is False:
            print('Введите категорию и цену через пробел!')

        elif user_selection(user_input):
            user_category, user_price = user_selection(user_input)
            if is_question(user_category, user_price) is False:
                print(f'Вы уже использовали данное задание.')
            else:
                user_answer = input(is_question(user_category, user_price))
                # проверяем наличие темы и цены, а затем получаем ответ от пользователя
                print(checking_user_answer(user_answer, user_category, user_price))
                # проверяем ответ пользователя и начисляем баллы
    print('Вопросов больше нет')

    #TODO надо подсчитать очки и сделать сброс JSON-а
