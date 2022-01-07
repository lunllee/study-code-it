# 오늘은 2019년 10월 29일 입니다.
year = 2019
month = 10
day = 29

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일 입니다.")

print("오늘은 {}년 {}월 {}일 입니다.".format(year, month, day))

day_string = "오늘은 {}년 {}월 {}일 입니다."
print(day_string.format(year, month, day))

print("저는 {1}, {0}, {2}를 좋아 합니다!".format("박지성", "유재석", "빌 게이츠"))

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))


name = "최지웅"
age = 32
# 가장 오래된 방식 (%기호)
print("제 이름은 %s이고 %d살 입니다." % (name, age))

# 많이 쓰는 방식(format 메소드)
print("제 이름은 {}이고 {}살 입니다.".format(name, age))

# 새로운 방식(f-string)
print(f"제 이름은 {name}이고 {age}살 입니다.")
