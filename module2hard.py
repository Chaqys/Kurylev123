while True:
    numbers = int(input('Введите число от 3 до 20: '))
    result = ''

    for i in range(1, numbers):
        for j in range(i+1, numbers):
            if numbers % (i+j) == 0:
                result += f'{i}{j}'
    print(f'{numbers} = {result}')
