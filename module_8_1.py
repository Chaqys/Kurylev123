def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError:
        print(str(a)+str(b))
def main():
    add_everything_up(123.456, 'строка')
    add_everything_up('яблоко', 4215)
    add_everything_up(123.45, 7)

if __name__ == '__main__':
    main()