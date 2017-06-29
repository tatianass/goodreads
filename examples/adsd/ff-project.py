import time
from goodreads import client
import json

def singleArray(inputlist):
    outputlist = []
    for i in inputlist:
      outputlist.extend(i)
    return outputlist

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

#define starting time
start_time = time.time()

books_number = input("Enter the max number of books in the search: ")
#authetification
gc = client.GoodreadsClient('fCUHaHylHEkSW3jJcZJTQ', 'dOKwd2Kewa5sIpoAynUEVl44s5wscrwWoAiGwBuijTI')

#get all books by query
books = gc.search_books_all_pages('Lesbian', search_field='genre')

print("get books from goodreads --- %s seconds ---" % (time.time() - start_time))

#parse books to single array
books = singleArray(books)

#to json
data = []
n_books = 0
for book in books:
    if(n_books == books_number): break
    i = {}
    i['isbn'] = book.isbn
    i['isbn13'] = book.isbn13
    i['title'] = book.title
    i['author'] = book.authors[0].name
    i['link'] = book.link
    i['popular_shelves'] = book.popular_shelves
    data.append(i)
    n_books = n_books + 1
    
writeToJSONFile('./','ff-books',data)
print("--- %s seconds ---" % (time.time() - start_time))
