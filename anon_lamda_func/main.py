def main():
    numbers = [1, 2, 5, 4, 7, 88, 12, 15, 55, 77, 95]

    even_numbers = filter(lambda number: True if number % 2 == 0 else False, numbers)

    print(list(even_numbers))


if __name__ == '__main__':
    main()

# [2, 4, 88, 12]