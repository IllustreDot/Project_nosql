import tkinter as tk
from tkinter import messagebox

neo4j_driver = None
mongoDB_driver = None
#1
def donner_nombre_utilisateurs():
    global mongoDB_driver
    c=mongoDB_driver.db.user.count_documents({})
    messagebox.showinfo("Nombre d'utilisateurs", f"Nombre d'utilisateurs: {c}")
#2
def donner_nombre_tweets():
    global mongoDB_driver
    c=mongoDB_driver.db.tweet.count_documents({})
    messagebox.showinfo("Nombre de tweets", f"Nombre de tweets: {c}")
#3
def donner_nombre_hashtags():
    global mongoDB_driver
    c=mongoDB_driver.db.tweet_hashtag.count_documents({})
    messagebox.showinfo("Nombre de tweets", f"Nombre de tweets: {c}")
#4
def donner_nombre_tweets_actualite():
    global mongoDB_driver
    c=mongoDB_driver.db.tweet_hashtag.count_documents({"hashtag":"actualité"})
    messagebox.showinfo("Nombre de tweets avec #actualité", f"Nombre de tweets avec #actualité: {c}")
#5
def donner_utilisateurs_différents_hashtag_IUT():
    global mongoDB_driver
    c=mongoDB_driver.db.tweet_hashtag.count_documents({"hashtag": "socionoel"})
    #print(c)
    #c=mongoDB_driver.db.tweet_hashtag.distinct("idUser",{"hashtag":"socionoel"})
    messagebox.showinfo("Utilisateurs différents avec #IUT", f"Nombre d'utilisateurs différents avec #IUT: {c}")
#6
def donner_tweets_reponses():
    global mongoDB_driver
    c=mongoDB_driver.db.tweet.find({"replyIdTweet": {"$nin": [float('NaN')]}})
    str=''
    for tweet in c:
        str+=f"Tweet: {tweet['idTweet']} - Réponse à: {int(tweet['replyIdTweet'])}\n"
    messagebox.showinfo("Différents tweets qui sont des réponses", f"Nombre de tweets qui sont des réponses: {str}")
#7
def donner_followers_BenAbdelazizC():
    global neo4j_driver
    global mongoDB_driver
    id=mongoDB_driver.db.user.find_one({"screenName":"BenAbdelazizC"})['idUser']
    with neo4j_driver.session() as session:
        query = f"""
        MATCH (u:User )-[:FOLLOW]->(f:User{{idUser: {id}}})
        RETURN u
        """
        c=session.run(query)

    str=''
    for record in c:
        r=mongoDB_driver.db.user.find_one({"idUser":record['u']['idUser']})
        str+=f"{r['screenName']}\n"

    messagebox.showinfo(f"Followers de BenAbdelazizC: {str}")
#8
def donner_utilisateurs_suivis_UCA():
    global neo4j_driver
    query = """
    MATCH (u:User {screenName: 'UCA'})-[:FOLLOW]->(followedUser)
    RETURN followedUser.screenName AS FollowedUser
    """
    with neo4j_driver.session() as session:
        result = session.run(query)
        followed_users = [record['FollowedUser'] for record in result]
    messagebox.showinfo("Utilisateurs suivis par UCA", "\n".join(followed_users) if followed_users else "Il y a aucun utilisateur suivi par UCA.")
#9
def donner_followers_et_followees_UCA():
    global neo4j_driver
    query = """
    MATCH (u:User {screenName: 'UCA'})<-[:FOLLOW]->(mutualUser)
    RETURN mutualUser.screenName AS MutualUser
    """
    with neo4j_driver.session() as session:
        result = session.run(query)
        mutual_users = [record['MutualUser'] for record in result]
    messagebox.showinfo("Followers et followees de UCA", "\n".join(mutual_users) if mutual_users else "Il y a aucun followers et followees mutuelle de UCA.")
#10
def donner_utilisateurs_plus_10_followers():
    global neo4j_driver
    query = """
    MATCH (u:User)<-[:FOLLOW]-(follower)
    WITH u, COUNT(follower) AS followerCount
    WHERE followerCount > 10
    RETURN u.screenName AS User, followerCount
    """
    with neo4j_driver.session() as session:
        result = session.run(query)
        users = [f"{record['User']} ({record['followerCount']} followers)" for record in result]
    messagebox.showinfo("Utilisateurs avec plus de 10 followers", "\n".join(users) if users else "Aucun utilisateur a plus que 10 followers.")
#11
def donner_utilisateurs_plus_5_suivis():
    global neo4j_driver
    query = """
    MATCH (u:User)-[:FOLLOW]->(followed)
    WITH u, COUNT(followed) AS followedCount
    WHERE followedCount > 5
    RETURN u.screenName AS User, followedCount
    """
    with neo4j_driver.session() as session:
        result = session.run(query)
        users = [f"{record['User']} (follows {record['followedCount']} users)" for record in result]
    messagebox.showinfo("Utilisateurs qui suivent plus de 5 utilisateurs", "\n".join(users) if users else "Il y a aucun user qui suit plus de 5 utilisateurs.")
#12
def donner_tweets_plus_populaires():
    global mongoDB_driver
    tweets = list(mongoDB_driver.db.tweet.find().sort("nbRetweet", -1).limit(10))
    tweet_texts = [f"{tweet['text']} (Retweets: {tweet['nbRetweet']})" for tweet in tweets]
    messagebox.showinfo("10 tweets les plus populaires", "\n".join(tweet_texts) if tweet_texts else "Aucun tweet populaire trouvé.")
#13
def donner_hashtags_plus_populaires():
    global mongoDB_driver
    hashtags = list(mongoDB_driver.db.tweet_hashtag.aggregate([
        {"$group": {"_id": "$hashtag", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]))
    popular_hashtags = [f"#{hashtag['_id']} ({hashtag['count']} uses)" for hashtag in hashtags]
    messagebox.showinfo("10 hashtags les plus populaires", "\n".join(popular_hashtags) if popular_hashtags else "Aucun hashtag populaire trouvé.")
#14
def donner_tweets_discussion():
    global mongoDB_driver
    tweets = list(mongoDB_driver.db.tweet.find({"replyIdTweet": {"$ne": None}}))
    discussion_tweets = [tweet['text'] for tweet in tweets]
    messagebox.showinfo("Tweets qui initient une discussion", "\n".join(discussion_tweets) if discussion_tweets else "Aucune tweet qui initie une discussion a été trouvé.")
#15
def plus_longue_discussion():
    global mongoDB_driver
    pipeline = [
        {"$match": {"replyIdTweet": {"$ne": None}}},
        {"$group": {"_id": "$replyIdTweet", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 1}
    ]
    longest_discussion = list(mongoDB_driver.db.tweet.aggregate(pipeline))
    if longest_discussion:
        root_tweet_id = longest_discussion[0]['_id']
        count = longest_discussion[0]['count']
        messagebox.showinfo("Plus longue discussion", f"Tweet ID: {root_tweet_id} avec {count} réponse.")
    else:
        messagebox.showinfo("Plus longue discussion", "Aucune discussions trouvé.")
#16
def debut_fin_conversations():
    global mongoDB_driver
    pipeline = [
        {"$match": {"replyIdTweet": {"$ne": None}}},
        {"$group": {"_id": "$replyIdTweet", "firstReply": {"$min": "$createdAt"}, "lastReply": {"$max": "$createdAt"}}}
    ]
    conversations = list(mongoDB_driver.db.tweet.aggregate(pipeline))
    conversation_details = [f"Root Tweet ID: {c['_id']}, Start: {c['firstReply']}, End: {c['lastReply']}" for c in conversations]
    messagebox.showinfo("Début et fin des conversations", "\n".join(conversation_details) if conversation_details else "Aucune conversations trouvé.")


def launch_app(driverMongo,driverNeo4j):
    global mongoDB_driver
    global neo4j_driver
    mongoDB_driver = driverMongo
    neo4j_driver = driverNeo4j
    root = tk.Tk()
    root.title("Application de Gestion des Tweets")

    # Create a frame for the buttons
    frame = tk.Frame(root)
    frame.pack(pady=10)

    # Create and place buttons in the frame
    buttons_texts = [
        "1. Donner le nombre des utilisateurs",
        "2. Donner le nombre de tweets",
        "3. Donner le nombre d'hashtags",
        "4. Donner le nombre de tweets contenant le hashtag actualité",
        "5. Donner le nombre d'utilisateurs différents qui ont tweeté un tweet contenant le hashtag IUT",
        "6. Donner les tweets qui sont des réponses à un autre tweet",
        "7. Donner le nom des followers de BenAbdelazizC",
        "8. Donner le nom des utilisateurs suivis par UCA",
        "9. Donner le nom des utilisateurs qui sont à la fois followers et followees de UCA",
        "10. Donner les utilisateurs ayant plus de 10 followers",
        "11. Donner les utilisateurs qui follows plus de 5 utilisateurs",
        "12. Donner les 10 tweets les plus populaires",
        "13. Donner les 10 hashtags les plus populaires",
        "14. Donner les tweets qui initient une discussion",
        "15. Quelle est la plus longue discussion ?",
        "16. Pour chaque conversation, donnez-en le début et la fin."
    ]

    # Function mapping
    functions = [
        donner_nombre_utilisateurs,
        donner_nombre_tweets,
        donner_nombre_hashtags,
        donner_nombre_tweets_actualite,
        donner_utilisateurs_différents_hashtag_IUT,
        donner_tweets_reponses,
        donner_followers_BenAbdelazizC,
        donner_utilisateurs_suivis_UCA,
        donner_followers_et_followees_UCA,
        donner_utilisateurs_plus_10_followers,
        donner_utilisateurs_plus_5_suivis,
        donner_tweets_plus_populaires,
        donner_hashtags_plus_populaires,
        donner_tweets_discussion,
        plus_longue_discussion,
        debut_fin_conversations
    ]

    # Create and place buttons in the frame
    for i, text in enumerate(buttons_texts):
        button = tk.Button(frame, text=text, command=functions[i])
        button.grid(row=i // 4, column=i % 4, padx=5, pady=5)

    # Start the GUI event loop
    root.mainloop()
