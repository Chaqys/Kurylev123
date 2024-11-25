#1st program
x = int((9**0.5)*5)
print(x)
#2nd program
x = 9.99 > 9.98 and 1000 != 1000.1
print(x)
#3rd program
result1 = 2 * 2 + 2
print(result1)

result2 = 2 * (2 + 2)
print(result2)

comparison = result1 == result2
print(comparison)

#4th program
x = '123.456'
print(x[4])

number_float = float(x)
number_scaled = number_float * 10
remainder = int(number_scaled) % 10
print(f"Смещение: {number_scaled}")
print(f"Первая цифра после запятой: {remainder}")