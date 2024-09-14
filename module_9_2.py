first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [len(res) for res in first_strings if len(res) > 5]
second_result = [(res_1,res_2) for res_1 in first_strings for res_2 in second_strings if len(res_1) == len(res_2)]
third_result = {res:len(res) for res in (first_strings + second_strings) if (len(res) % 2) == 0}
print(first_result)
print(second_result)
print(third_result)

