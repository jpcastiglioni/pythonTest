def main():
    programming_books = {
        'C Programming Language': 35,
        'Introduction to Algorithms': 100,
        'Clean Code: A Handbook of Agile Software Craftsmanship': 50
    }

    cpl = 'C Programming Language'
    algo = 'Introduction to Algorithms'
    key = 'C Programming Language'

    print(f"The price of {cpl} is ${programming_books.get(cpl)}")
    print(f"The price of {algo} is ${programming_books[algo]}")

    programming_books[key] = 45

    programming_books['The Pragmatic Programmer'] = 32

    print(programming_books)
    print(programming_books.popitem())

    key = 'C Programming Language'

    print(programming_books.pop(key))

    print(programming_books)


    programming_books.clear()

    print(programming_books)

if __name__ == '__main__':
    main()