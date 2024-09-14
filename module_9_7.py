
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result % 2:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    total = 0
    for summ in args:
        total += summ
    return total


result = sum_three(2, 3, 6)
print(result)