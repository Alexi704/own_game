from functions import data_output_screen, user_selection, is_question, checking_user_answer, check_answer, \
    game_total_score
from convert_to_json import convert_to_json


if __name__ == '__main__':

    while check_answer() is False:
        print(data_output_screen())  # выводим на экран наши темы и цены
        user_input = input('Выбирайте категорию вопроса и цену:\n')

        if user_selection(user_input) is False:
            print('Введите категорию и цену через пробел!')

        elif user_selection(user_input):
            user_category, user_price = user_selection(user_input)
            if is_question(user_category, user_price) is False:
                pass
            else:
                user_answer = input(is_question(user_category, user_price))
                # проверяем наличие темы и цены, а затем получаем ответ от пользователя
                print(checking_user_answer(user_answer, user_category, user_price))
                # проверяем ответ пользователя и начисляем баллы

    print(game_total_score())

    convert_to_json() # преобразуем данные в исходное состояние


