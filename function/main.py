def hello(message, is_lower=False):
    if is_lower:
        return message.lower()
    else:
        return message.upper()

def total(numbers):
    s = 0
    for number in numbers:
        s += number
    return s

def total2(*args):
    print(type(args))

    t = 0
    for arg in args:
        t += arg

    return t

def items(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f"{key} : {value}")

def main():
    uppercase_message = hello('Hello, Universe!')
    print(uppercase_message)

    lowercase_message = hello('Hello, Universe!', True)
    print(lowercase_message)

    print(total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    print(total2(1, 2, 3, 4, 5))

    items(
        Apple=10,
        Orange=8,
        Grape=35
    )

if __name__ == '__main__':
    main()

# HELLO, UNIVERSE!
# hello, universe!