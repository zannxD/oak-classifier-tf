from eval import eval
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from pymongo import MongoClient
from bson.objectid import ObjectId

 
client = MongoClient()
client = MongoClient("mongodb://dimuthu:123@ds149124.mlab.com:49124/oak")

app = Flask(__name__)
api = Api(app)

class SentimentalAnalysis(Resource):
    def get(self, comment):
         predictions = eval([comment])
         return {'sentiment': [i[1] for i in predictions]}

class MovieAnalysis(Resource):
    def get(self, movie_id):
         db = client.oak
         movie = db.movies.find_one({u'_id':ObjectId(movie_id) })
         if movie is None:
             return {'sentiment': false }
         else:
        
            predictions = eval(movie["comments"])
            neg = 0
            pos = 0
           
            for x in predictions:
                if(float(x[1]) >0):
                    pos= pos+1
                else:
                    neg= neg+1

            result = (pos>neg)
            print(result)
            return {'overall': result, 'pos': pos, 'neg': neg}

 
api.add_resource(SentimentalAnalysis, '/sentimental/<string:comment>')
api.add_resource(MovieAnalysis, '/movie/<string:movie_id>')

if __name__ == '__main__':
     app.run()