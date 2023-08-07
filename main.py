from untils import build_statistics, load_question, write_record, print_records
import random

way_records_txt = 'data/records.txt'
way_questions_json = 'data/questions.json'
name = None
if __name__ == '__main__':
    questions = load_question(way_questions_json)

    name = input("Как ваше имя: ")
    random.shuffle(questions)
    for item in questions:
        print(item.build_question())
        asked_user = input("Ваш ответ: ").lower().strip()
        item.user_answer = asked_user
        print(item.build_feedback())

    result, score = build_statistics(questions)
    print(result)
    write_record(way_records_txt, name, score)

    print("Показать все рекорды? (да)/(нет)")
    agree = input(": ")
    if agree == 'да':
        for item in print_records(way_records_txt, agree):
            print(item)
    else:
        print("Еще увидимся!")



