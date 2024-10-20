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
    messagebox.showinfo("Nombre de tweets qui sont des réponses", f"Nombre de tweets qui sont des réponses: {str}")
#7
def donner_followers_IUT():
    messagebox.showinfo("Followers de IUT", "Fonction 7: Liste des followers de IUT ici.")

def donner_utilisateurs_suivis_UCA():
    messagebox.showinfo("Utilisateurs suivis par UCA", "Fonction 8: Liste des utilisateurs suivis par UCA ici.")

def donner_followers_et_followees_UCA():
    messagebox.showinfo("Followers et followees de UCA", "Fonction 9: Liste des utilisateurs qui sont à la fois followers et followees de UCA ici.")

def donner_utilisateurs_plus_10_followers():
    messagebox.showinfo("Utilisateurs avec plus de 10 followers", "Fonction 10: Liste des utilisateurs avec plus de 10 followers ici.")

def donner_utilisateurs_plus_5_suivis():
    messagebox.showinfo("Utilisateurs qui suivent plus de 5 utilisateurs", "Fonction 11: Liste des utilisateurs qui suivent plus de 5 utilisateurs ici.")

def donner_tweets_plus_populaires():
    messagebox.showinfo("10 tweets les plus populaires", "Fonction 12: Liste des 10 tweets les plus populaires ici.")

def donner_hashtags_plus_populaires():
    messagebox.showinfo("10 hashtags les plus populaires", "Fonction 13: Liste des 10 hashtags les plus populaires ici.")

def donner_tweets_discussion():
    messagebox.showinfo("Tweets qui initient une discussion", "Fonction 14: Liste des tweets qui initient une discussion ici.")

def plus_longue_discussion():
    messagebox.showinfo("Plus longue discussion", "Fonction 15: Détails de la plus longue discussion ici.")

def debut_fin_conversations():
    messagebox.showinfo("Début et fin des conversations", "Fonction 16: Détails sur le début et la fin de chaque conversation ici.")


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
        "7. Donner le nom des followers de IUT",
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
        donner_followers_IUT,
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
