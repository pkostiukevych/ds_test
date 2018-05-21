def author_serializer(author):

    return {
        'id': author.id,
        'first_name': author.first_name,
        'middle_name': author.middle_name,
        'last_name': author.last_name,
        'full_name': author.full_name()
    }


def book_serializer(book):
    return {
        'id': book.id,
        'title': book.title,
        'authors': list(map(author_serializer, book.authors.all())),
        'isbn': book.isbn or '',
        'price': book.price,
        'publish_date': book.publish_date
    }