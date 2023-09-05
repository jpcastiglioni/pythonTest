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

def main():
    uppercase_message = hello('Hello, Universe!')
    print(uppercase_message)

    lowercase_message = hello('Hello, Universe!', True)
    print(lowercase_message)

    print(total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

if __name__ == '__main__':
    main()

# HELLO, UNIVERSE!
# hello, universe!