import random


def success_message():
    print('맞았습니다!\n')


def fail_message(a):
    print(f'아쉽습니다. 정답은 {a}입니다.\n')


with open('vocabulary.txt', 'r', encoding='UTF-8') as f:
    dic = {}
    for line in f:
        qa = line.strip().split(": ")
        dic[qa[1]] = qa[0]

    while len(dic) != 0:
        q = random.choice(list(dic.keys()))
        a = input(f'{q}: ')
        if a.strip() == dic[q]:
            success_message()
        elif a.strip() == 'q':
            break
        else:
            fail_message(dic[q])

