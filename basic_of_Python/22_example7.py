def success_message():
    print('맞았습니다!\n')


def fail_message(a):
    print(f'아쉽습니다. 정답은 {a}입니다.\n')


with open('vocabulary.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        qa = line.strip().split(": ")
        answer = input(f'{qa[1]} :')
        if answer == qa[0]:
            success_message()
        else:
            fail_message(qa[0])

