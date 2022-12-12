import json

question = {
    'Транспорт': {
        '100': {'question': 'plane', 'answer': 'самолет', 'asked': False},
        '200': {'question': 'train', 'answer': 'поезд', 'asked': False},
        '300': {'question': 'boarding', 'answer': 'посадка', 'asked': False}
    },
    'Животные': {
        '100': {'question': 'dog', 'answer': 'собака', 'asked': False},
        '200': {'question': 'shark', 'answer': 'акула', 'asked': False},
        '300': {'question': 'sparrow', 'answer': 'воробей', 'asked': False}
    },
    'Еда': {
        '100': {'question': 'apple', 'answer': 'яблоко', 'asked': False},
        '200': {'question': 'berry', 'answer': 'ягода', 'asked': False},
        '300': {'question': 'venison', 'answer': 'оленина', 'asked': False}
    },
}

raw_json = json.dumps(question, ensure_ascii=False, indent=4)
print(raw_json)

with open('questions.json', 'w', encoding='utf-8') as file:
    file.write(raw_json)
