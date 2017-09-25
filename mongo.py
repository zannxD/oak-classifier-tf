from pymongo import MongoClient

client = MongoClient()
client = MongoClient("mongodb://dimuthu:123@ds149124.mlab.com:49124/oak")

db = client.oak
movies = db.movies

#movies = coll.find()

for m in movies.find():
    print("Movie: ",m["name"],"-----------Overall Opinion: ",m["overall_opinion"])
    
    
print ('\nNumber of movies', movies.count())


#print ('\nOne movie only' )   
#print (movies.find_one())