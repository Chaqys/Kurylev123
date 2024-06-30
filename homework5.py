immutable_var = 1 , True , 'apple' , False , 3 , 5
print(immutable_var)
#immutable_var[2] = 140
print('Элементы кортежа неизменяемы объекты, именно поэтому при попытке его изменить, будет выдавать ошибку')
mutable_list = [195, 589, 'apple' , 'juice']
print((mutable_list))
mutable_list[3]="soda"
print(mutable_list)