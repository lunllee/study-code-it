# 사전 (dictionary)
# key-value pair (키-값 쌍)
my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}
print(my_dictionary[5])

my_family = {
    '어머니': '어머니 이름',
    '아버지': '아버지 이름',
    '아들': '아들 이름',
    '딸': '딸 이름'
}
print(my_family['아버지'])
print('아들 이름' in my_family.values())
print('아들' in my_family.values())

for value in my_family.values():
    print(value)

for key in my_family.keys():
    value = my_family[key]
    print(key, value)

for key, value in my_family.items():
    print(key, value)

