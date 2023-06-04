from pymongo import MongoClient
import certifi

#importando paquetes para la coneccion a mongo 
MONGO_URI = 'mongodb+srv://jv2208674:#puteria @pythonflask.evxx3an.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

#Funcion para conectarse a mongo con los paquetes instalados 
def conection_db():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile = ca)
        db = client['dbd_CRUD']
    except ConnectionError:
        print('Error al  conectarse')
    return db
