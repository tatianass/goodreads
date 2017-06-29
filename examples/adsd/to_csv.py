import time
import unicodecsv as csv
import json

#define starting time
start_time = time.time()

books_number = input("Enter the max number of books in the search: ")

n_books = 0
with open('ff-books-genre.json') as data_file:
    books = json.load(data_file)
    with open('ff-books.csv', 'wb') as csvfile:
        fieldnames = ['isbn', 'title', 'author', 'shelve']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for book in books:
            if(n_books == books_number): break
            shelves = book['popular_shelves']
            for shelve in shelves:
                i = {}
                i['isbn'] = book['isbn']
                i['title'] = book['title']
                i['author'] = book['author']
                i['shelve'] = shelve
                writer.writerow(i)
            n_books = n_books + 1

print("--- %s seconds ---" % (time.time() - start_time))

