from question import Question
import json


def load_question(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        list_questions = json.load(file)

    question = []
    for item in list_questions:
        text = item['q']
        difficulty = item['d']
        correct_answer = item['a']
        view = Question(text, difficulty, correct_answer)
        question.append(view)

    return question


def build_statistics(question):
    score = 0
    count = 0
    for item in question:
        if item.is_correct():
            score += item.score
            count += 1

    return f"Вот и всё!\nОтвечено {count} вопроса из {len(question)}\nНабрано баллов: {score}\n", score


def write_record(filename, name, score):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"Имя: {name}, Баллы: {score}\n")


def print_records(text_txt, agree):
    list_records = []
    with open(text_txt, 'r', encoding='utf-8') as file:
        view = file.readlines()
    for item in view:
        list_records.append(item.strip('\n'))
    if agree:
        return list_records
