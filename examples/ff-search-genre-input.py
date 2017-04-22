from goodreads import client
import json

genres = ["action","anthology","art","autobiographies","biographies","childrens","comics","cookbooks","diary","dictionaries","drama","fantasy","health","history","horror","journal","mystery","poetry","romance","science-fiction","self-help","travel","sci-fi"]
genresWithHyphen = ["science-fiction","self-help","sci-fi"]

#split shelves
def splitShelves(shelves):
    output = []
    for shelve in shelves:
        if(shelve in genresWithHyphen):
            output.append(shelve)
        else:
            output.extend(shelve.split("-"))
    
    return output
                      
#write object to json
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
        
#check genre
def checkGenre(shelves, genre):
    return genre in shelves

#authetification
gc = client.GoodreadsClient('fCUHaHylHEkSW3jJcZJTQ', 'dOKwd2Kewa5sIpoAynUEVl44s5wscrwWoAiGwBuijTI')

#get all books by query
books = gc.search_books_all_pages('Lesbian', search_field='genre')

#to json
data = {"action":[],"anthology":[],"art":[],"autobiographies":[],"biographies":[],"childrens":[],"comics":[],"cookbooks":[],"diary":[],"dictionaries":[],"drama":[],"fantasy":[],"health":[],"history":[],"horror":[],"journal":[],"mystery":[],"poetry":[],"romance":[],"science-fiction":[],"self-help":[],"travel":[],"sci-fi":[]}
for book in books:
    shelves = splitShelves(book.popular_shelves)
    for genre in genres:
        if(checkGenre(shelves, genre)):
            i = {}
            i['title'] = book.title
            i['author'] = str(book.authors[0])
            data[genre].append(i)      
writeToJSONFile('./', 'genre', data)
