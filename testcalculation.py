input = input("Enter: ") #แรกะะะะะะะะะะ
for i in input:
    if i == "+":
        lst = input.split("+")
        print(int(lst[0]) + int(lst[1]))

    if i == "-":
        lst = input.split("-")
        print(int(lst[0]) - int(lst[1]))

    if i == "*":
        lst = input.split("*")
        print(int(lst[0]) * int(lst[1]))

    if i == "/":
        lst = input.split("/")
        print(int(lst[0]) / int(lst[1]))

    print("----------------------")
