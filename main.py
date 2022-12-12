from functions import data_output_screen, user_selection


if __name__ == '__main__':

    print(data_output_screen())
    # user_input = input('Выбирайте категорию вопроса и цену:\n')
    user_input = ' ЕДА 100  '
    user_category, user_price = user_selection(user_input)
    print(user_category)
    print(user_price)
