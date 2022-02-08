
with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line.strip())

# strip
my_string = "            111   asd      "
print(my_string.strip())

# split
my_string2 = "1. 2. 3. 4. 5. 6"
print(my_string2.split(". "))

full_name = "Kim, Yuna"
name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]
print(last_name, first_name)
