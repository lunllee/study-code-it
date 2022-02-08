name = input("이름을 입력 하세요 : ")
print(name)

x = input("숫자를 입력 하세요 : ")
print(int(x))


import random

r_num = random.randint(1, 20)
try_num = 4
# print(r_num)
while try_num > 0:
    try_num -= 1
    input_num = input(f"기회가 {try_num}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ")
    if r_num == int(input_num):
        result_num = 4 - try_num
        print(f"축하합니다. {result_num}번 만에 숫자를 맞히셨습니다.")
        break
    else:
        if int(input_num) < int(r_num):
            print("Up")
        else:
            print("Down")

        if try_num == 0:
            print(f"아쉽습니다. 정답은 {r_num}였습니다.")
