from mathstuff import natural_sum as nsum


def main():
    last_number = int(input('up to which number would you like to calculate the sum?\n- '))

    print(nsum(last_number))


if __name__ == '__main__':
    main()

# up to which number would you like to calculate the sum?
# - 10
# 55