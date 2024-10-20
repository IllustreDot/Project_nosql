from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from neo4j import GraphDatabase
from urllib.parse import quote_plus

def connection_mongodb(uri):
    try:
        client = MongoClient(uri)
        print("Connexion réussie à MongoDB !")
        return client
    except ConnectionFailure as e:
        print(f"Échec de connexion à MongoDB : {e}")
        return None

def connection_neo4j(uri, user, password):
    try:
        driver = GraphDatabase.driver(uri, auth=(user, password))
        print("Connexion réussie à Neo4j !")
        return driver
    except Exception as e:
        print(f"Échec de connexion à Neo4j : {e}")
        return None

def neo4j():
    neo4j_uri =""
    neo4j_user = ""
    neo4j_password = ""
    neo4j_driver = connection_neo4j(neo4j_uri, neo4j_user, neo4j_password)
    return neo4j_driver

def mongoDB():
    username = quote_plus('')
    password = quote_plus('')
    mongo_uri = ''
    mongodb_driver = connection_mongodb(mongo_uri)
    return mongodb_driver