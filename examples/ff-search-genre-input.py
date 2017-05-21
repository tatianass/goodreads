import json

genres = ["20th-century","21st-century","3-stars","4-stars","5-stars","action","adult","adventure","age-gap","anthology","art","audiobook","autobiography","bdsm","biography","businesswoman","celebrity","classics","college","comedy","comics","coming-of-age","coming-out","contemporary","crime","crime-mystery","criminal","dark","detective","disability","diversity","drama","dystopian","ebook","erotica","family","fantasy","favorites","favorite-series","fiction","friendship","historical","horror","humor","kids","law-enforcement","magic","medical","memoir","military","mystery","no-for-kids","non-fiction","paranormal","poetry","politics","psychology","relationships","religion","rich-girl-poor-girl","school","science-fiction","series","shapeshifters","short-stories","stand-alone","supernatural","suspense","thriller","trans","urban-fantasy","vampires","werewolves","young-adult"]
                      
#write object to json
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
        
#check genre
def checkGenre(shelves, genre):
    return genre in shelves

#to json
data = {"20th-century": [],"21st-century": [],"3-stars": [],"4-stars": [],"5-stars": [],"action": [],"adult": [],"adventure": [],"age-gap": [],"anthology": [],"art": [],"audiobook": [],"autobiography": [],"bdsm": [],"biography": [],"businesswoman": [],"celebrity": [],"classics": [],"college": [],"comedy": [],"comics": [],"coming-of-age": [],"coming-out": [],"contemporary": [],"crime": [],"crime-mystery": [],"criminal": [],"dark": [],"detective": [],"disability": [],"diversity": [],"drama": [],"dystopian": [],"ebook": [],"erotica": [],"family": [],"fantasy": [],"favorites": [],"favorite-series": [],"fiction": [],"friendship": [],"historical": [],"horror": [],"humor": [],"kids": [],"law-enforcement": [],"magic": [],"medical": [],"memoir": [],"military": [],"mystery": [],"no-for-kids": [],"non-fiction": [],"paranormal": [],"poetry": [],"politics": [],"psychology": [],"relationships": [],"religion": [],"rich-girl-poor-girl": [],"school": [],"science-fiction": [],"series": [],"shapeshifters": [],"short-stories": [],"stand-alone": [],"supernatural": [],"suspense": [],"thriller": [],"trans": [],"urban-fantasy": [],"vampires": [],"werewolves": [],"young-adult": []}
with open('ff-books.json') as data_file:
    books = json.load(data_file)
    for book in books:
        shelves = book['popular_shelves']
        for genre in genres:
            if(checkGenre(shelves, genre)):
                i = {}
                i['isbn'] = book['isbn']
                i['isbn13'] = book['isbn13']
                i['title'] = book['title']
                i['author'] = book['author']
                i['link'] = book['link']
                data[genre].append(i)      
writeToJSONFile('./', 'genre', data)
