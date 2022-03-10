import random


def pick_num_return_list(n):
    result = []
    while len(result) < n:
        pick_num = random.randint(0, 9)
        if pick_num not in result:
            result.append(pick_num)

    # print(result)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return result


def match_list(list_1, list_2):
    s = 0
    b = 0
    for y in range(3):
        if list_1[y] == list_2[y]:
            s += 1
        elif list_1[y] in list_2:
            b += 1

    print(f"{s}S {b}B\n")
    return s


def main():
    result = pick_num_return_list(3)
    select = []
    run_count = 0

    while True:
        run_count += 1
        print("숫자 3개를 하나씩 차례대로 입력하세요.")

        while len(select) < 3:
            select_num = int(input(f"{len(select)+1}번째 숫자를 입력하세요: "))
            if int(select_num) not in range(0, 10):
                print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            elif select_num not in select:
                select.append(select_num)
            else:
                print("중복되는 숫자 입니다. 다시 입력하세요.")

        # print(select)
        strike = match_list(result, select)

        if strike == 3:
            print(f"축하합니다. {run_count}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.")
            break
        else:
            select = []


main()
