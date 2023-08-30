def main():
    numbers = {1, 2, 3, 4, 5}

    for number in numbers:
        print(number)

    numbers = {}

    print(type(numbers))

    numbers = set()

    print(type(numbers))

if __name__ == '__main__':
    main()