import pandas as pd

def load_twitter_data_to_mongodb(tweet,user,tweet_hashtag,driver):
    #tweet
    df = pd.read_csv(tweet,delimiter='<')
    for index, row in df.iterrows():
        tweet = {
            "idTweet": row['idTweet'],
            "idUser": row['idUser'],
            "replyIdTweet": row['replyIdTweet'],
            "replyIdUser": row['replyIdUser'],
            "quotedIdTweet": row['quotedIdTweet'],
            "quotedIdUser": row['quotedIdUser'],
            "text": row['text'],
            "createdAt": row['createdAt'],
            "url": row['url'],
            "source": row['source'],
            "lang": row['lang'],
            "nbRetweet": row['nbRetweet'],
            "nbFavorites": row['nbFavorites']
        }
        driver.db.tweet.insert_one(tweet)
    
    #user
    df = pd.read_csv(user,delimiter='	')
    for index, row in df.iterrows():
        user = {
            "idUser": row['idUser'],
            "screenName": row['screenName'],
            "name": row['name'],
            "description": row['description'],
            "createdAt": row['createdAt'],
            "url": row['url'],
            "location": row['location'],
            "lang": row['lang'],
            "nbStatuses": row['nbStatuses'],
            "nbFavorites": row['nbFavorites'],
            "nbFollowers": row['nbFollowers'],
            "nbFollowing": row['nbFollowing']
        }
        driver.db.user.insert_one(user)
        
    #tweet_hashtag
    df = pd.read_csv(tweet_hashtag,delimiter='	')
    for index, row in df.iterrows():
        tweet_hashtag = {
            "idTweet": row['idTweet'],
            "hashtag": row['hashtag'],
            "hashtagBrut": row['hashtagBrut'],
            "indiceStart": row['indiceStart'],
            "indiceEnd": row['indiceEnd']
        }
        driver.db.tweet_hashtag.insert_one(tweet_hashtag)

    return True

def load_data_mongoDB(driver):
    try:
        csv_file_path_tweet = 'TwitterData/tweet.csv'
        csv_file_path_user = 'TwitterData/tw_user.csv'
        csv_file_path_tweet_hashtag = 'TwitterData/tweet_hashtag.csv'
        load_twitter_data_to_mongodb(csv_file_path_tweet,csv_file_path_user,csv_file_path_tweet_hashtag,driver)
        print("Data loaded into MongoDB.")
        return True
    except Exception as e:
        print(f"Failed to load data into MongoDB: {e}")
        return False