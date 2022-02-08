# 파일을 작성할 땐 w, 계속 추가할 땐 a
# with open('data/new_file.txt', 'w', encoding='UTF-8') as f:
#     f.write('Hello world!\n')
#     f.write('My name is Codeit.\n')

with open('vocabulary.txt', 'w', encoding='UTF-8') as f:
    run = True
    dic = {}
    while run:
        voca = input("영어 단어를 입력하세요: ")
        if not voca.strip():
            print()
            continue
        elif voca == "q":
            for key, value in dic.items():
                # print(f"{key}: {value}")
                f.write(f"{key}: {value}\n")
            run = False
            break

        k_voca = input("한국어 뜻을 입력하세요: ")
        dic[voca] = k_voca
