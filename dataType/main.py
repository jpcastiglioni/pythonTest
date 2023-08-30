def main():
    book, author, release_year, goodreads_rating = 'Dracula', 'Bram Stoker', 1897, 4.01
    # book = 'Dracula'
    # author = 'Bram Stoker'
    # release_year = 1897
    # goodreads_rating = 4.01

    print(book, author, release_year, goodreads_rating)
    print(book + ' is a novel by ' + author + ', published in ' + str(release_year) + 
          '. It has a rating of ' + str(goodreads_rating) + ' on goodreads.')
    print(f'{book} is a novel by {author}, published in {release_year}.'
          f' It has a rating of {goodreads_rating} on goodreads.')
    # print(book)
    # print(author)
    # print(release_year)
    # print(goodreads_rating)


if __name__ == '__main__':
    main()
