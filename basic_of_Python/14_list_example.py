# 리스트 (list)
numbers = [2, 3, 5, 7, 11, 13]
names = ["윤수", "혜린", "태호", "영훈"]

# 인덱싱 (indexing)
print(names[0])
print(numbers[1] + numbers[3])
print(numbers[-1])
print(numbers[-2])

num_1 = numbers[1]
num_3 = numbers[3]

print(num_1 + num_3)

# 리스트 슬라이싱 (list slicing)
print(numbers[1:3])
print(numbers[:3])
print(numbers[1:])

# 리스트 값 변경
numbers[0] = 7
print(numbers[0])


numbers = []
print(len(numbers))

numbers.append(5)
numbers.append(8)
print(numbers)
print(len(numbers))

del numbers[0]
print(numbers)
print(len(numbers))

numbers.insert(4, 0)
numbers.insert(4, 1)
numbers.insert(4, 2)
print(numbers)


numbers = [19, 13, 2, 5, 3, 11, 7, 17]
new_list = sorted(numbers, reverse=True)
print(numbers)
print(new_list)

numbers.sort()
print(numbers.sort())
print(numbers)

numbers.sort(reverse=True)
print(numbers)

