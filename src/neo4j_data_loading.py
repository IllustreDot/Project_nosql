import pandas as pd

def load_twitter_data_to_neo4j(retweet,follow,driver):
    #retweet
    with driver.session() as session:
        df = pd.read_csv(retweet,delimiter='	')
        #idTweet,idRetweet
        for index, row in df.iterrows():
            tweet_id = row['idTweet']
            retweet_id = row['idRetweet']
            query = f"""
            MERGE (t:Tweet {{idTweet: {tweet_id}}})
            MERGE (r:Tweet {{idTweet: {retweet_id}}})
            CREATE (t)-[:RETWEET]->(r)
            """
            session.run(query)

        #follow
        df = pd.read_csv(follow,delimiter='	')
        #sourceIdUser,targetIdUser
        for index, row in df.iterrows():
            source_id = row['sourceIdUser']
            target_id = row['targetIdUser']
            query = f"""
            MERGE (s:User {{idUser: {source_id}}})
            MERGE (t:User {{idUser: {target_id}}})
            CREATE (s)-[:FOLLOW]->(t)
            """
            session.run(query)  
            
    return True




def load_data_neo4j(driver):
    try:
        retweet = 'TwitterData/tweet_retweet.csv'
        follow = 'TwitterData/tw_user_follow.csv'
        load_twitter_data_to_neo4j(retweet,follow,driver)
        print("Data loaded into Neo4j.")
        return True
    except Exception as e:
        print(f"Failed to load data into neo4j: {e}")
        return False