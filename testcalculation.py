input = input("Enter: ") #แรกกำหนดตัวแปร "input"  เมือกด Enter  ให้ให้แปรคำตอบออกมา
for i in input:          #
    if i == "+":
        lst = input.split("+")
        print(int(lst[0]) + int(lst[1])) #

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
