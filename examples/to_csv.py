import unicodecsv as csv
import json

with open('ff-books.json') as data_file:
    books = json.load(data_file)
    with open('ff-books.csv', 'wb') as csvfile:
        fieldnames = ['isbn', 'title', 'author', 'shelve']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for book in books:
            shelves = book['popular_shelves']
            for shelve in shelves:
                i = {}
                i['isbn'] = book['isbn']
                i['title'] = book['title']
                i['author'] = book['author']
                i['shelve'] = shelve
                writer.writerow(i)
