from pymongo import MongoClient
import certifi



MONGO_URI="mongodb+srv://matias:753159@cluster0.9ildljr.mongodb.net/?retryWrites=true&w=majority"
ca= certifi.where()

def dbconecction():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db= client['productos de la app']
    except ConnectionError:
        print("no se pudo conectar a la base de datos")
    return db