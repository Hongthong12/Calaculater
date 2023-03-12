while True:
    number_1 = int(input('frist number: \n'))
    operator = input('operator: \n')
    number_2 = int(input('frist number: \n'))

    if (operator == '+'):
        print("Rusult:", number_1 + number_2)
    elif (operator == '-'):
        print("Rusult:", number_1 - number_2)
    elif (operator == '*'):
        print("Rusult:", number_1 * number_2)
    elif (operator == '/'):
        print("Rusult:", number_1 / number_2)
    else:
        print('Try again')