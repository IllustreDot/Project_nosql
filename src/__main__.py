from app import launch_app
from connection import mongoDB
from connection import neo4j
from mongodb_data_loading import load_data_mongoDB
from neo4j_data_loading import load_data_neo4j

neo4j_driver = None
mongoDB_driver = None

def main():
    print("Running neo4j connection ...")
    global neo4j_driver
    neo4j_driver = neo4j()
    print("Running mongoDB connection ...")
    global mongoDB_driver
    mongoDB_driver = mongoDB()
    print("Connections established successfully.")

    choice=input("Do you want to load data into MongoDB? (y/n): ")
    if choice=='y':
        print("Loading data into MongoDB ...")
        load_data_mongoDB(mongoDB_driver)
    else:
        print("Data not loaded into MongoDB.")
    
    choice=input("Do you want to load data into Neo4j? (y/n): ")
    if choice=='y':
        print("Loading data into Neo4j ...")
        load_data_neo4j(neo4j_driver)
    else:
        print("Data not loaded into Neo4j.")
    
    print("Application booting up ...")
    launch_app(mongoDB_driver,neo4j_driver)


if __name__ == "__main__":
    main()