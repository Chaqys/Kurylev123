my_dict = {'Max': 1998, 'Sasha': 2000, 'Valya': 2005}
print(my_dict)
print(my_dict ['Max'])
print(my_dict.get('Vadim'))
my_dict.update({"Galina" : 2010,
                "Georg": 1955})
my_dict.pop('Sasha')
print(my_dict)

my_set = {586, True, 681,'Juice', 735, True,(1, 2, 3, 4),'Juice', 681, 735, True, 'Juice', 681, 'Python', (1, 2, 3, 4)}
print(my_set)
my_set.add('Max')
my_set.add(38)
my_set.discard('Juice')
print(my_set)

