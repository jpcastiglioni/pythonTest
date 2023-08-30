def main():
    name = input('What is your name? ')
    age = int(input(f'How old are you {name}? '))
    current_year = int(input(f'What year is this again? '))

    print(f'If my calculations are right, you were born in {current_year - age}')


if __name__ == '__main__':
    main()