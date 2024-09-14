first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = ((len(res_1) - len(res_2)) for res_1, res_2 in zip(first, second) if len(res_1) != len(res_2))
second_result =(len(first[res]) == len(second[res]) for res in range(len(first)))
print(list(first_result))
print(list(second_result))