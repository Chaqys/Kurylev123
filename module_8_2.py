def personal_sum(*numbers):
    incorrect_data = 0
    result = 0
    for number in numbers:
        for num in number:
            try:
                result += num
            except TypeError:
                incorrect_data += 1
                print(f'Неккоректный тип данных для подсчета сумм - {num}')
    return result, incorrect_data
def calculate_average(*numbers):
    if isinstance(*numbers, int):
        return None
    try:
        pers_sum = personal_sum(*numbers)
        return pers_sum[0] / (len(*numbers) - pers_sum[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        return f'В nubmers записан неккоректный тип данных'

def main():
    print(f'Результат 1: {calculate_average("1, 2, 3")}')
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
    print(f'Результат 3: {calculate_average(567)}')
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')


if __name__ == '__main__':
    main()



