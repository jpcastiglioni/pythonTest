def main():
    horror_books = ['Dracula', 'Carmilla', 'The Imago Sequence']

    print(horror_books.pop())
    horror_books.append('The Exorcist')
    print(horror_books)

    print(horror_books[0])
    print(horror_books[1])
    print(horror_books[-2])

    a_range = range(5, 15)

    print(a_range)

    list_a_range = list(a_range)

    tup_a_range = tuple(a_range)

    print(list_a_range)

    print(tup_a_range)

if __name__ == '__main__':
    main()
