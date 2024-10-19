# NoSQL Exploration

## Project 2024-2025

This project involves developing a Python application to interact with two NoSQL cloud databases: **MongoDB** (document-oriented) and **Neo4j** (graph-oriented).

### Objectives:

- Securely connect to MongoDB and Neo4j.
- Query MongoDB to retrieve, insert, update, and delete documents.
- Use Cypher query language to interact with Neo4j, create nodes and relationships, and perform path searches.
- Analyze and visualize data using libraries like Matplotlib and Seaborn (for MongoDB), and Neovis.js (for Neo4j).

### Data:

- MongoDB: Two collections, one for users and one for tweets.
- Neo4j: "Follow" and "Retweet" relationships between users and tweets, based on MongoDB IDs.

### Features to Implement:

- Statistics on the number of users, tweets, and hashtags.
- Search for tweets containing specific hashtags or replies to other tweets.
- Identify active users (followers, followees).
- Analyze conversations and find long or popular discussions (tweets, hashtags).
