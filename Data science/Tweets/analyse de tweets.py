import tweepy
import matplotlib.pyplot as plt
from textblob import TextBlob

# Ton Bearer Token
BEARER_TOKEN = "TON BEARER TOKEN"

client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Paramètres
search_term = input("Entrez le terme de recherche pour l'analyse des tweets : ")
langue_search = input("Entrez la langue des tweets (par exemple, 'fr' pour français) : ")
# par défaut, français
if not langue_search:
    langue_search = "fr"  
tweet_count = 50 

# Récupération des tweets récents en français
tweets = client.search_recent_tweets(
    query=f"{search_term} lang:{langue_search} -is:retweet",
    max_results=tweet_count,
    tweet_fields=["created_at", "lang"]
)

# Initialisation des compteurs
positive = 0
negative = 0
neutral = 0

if tweets.data:
    for tweet in tweets.data:
        analysis = TextBlob(tweet.text)
        if analysis.sentiment.polarity > 0:
            positive += 1
        elif analysis.sentiment.polarity < 0:
            negative += 1
        else:
            neutral += 1

    total_tweets = positive + negative + neutral

    # Création du camembert
    labels = ['Positif', 'Négatif', 'Neutre']
    sizes = [positive, negative, neutral]
    colors = ['#4CAF50', '#F44336', '#FFEB3B']
    explode = (0.1, 0, 0)  # mettre en valeur le positif

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title(f'Analyse de sentiment pour "{search_term}" ({total_tweets} tweets)')
    plt.axis('equal')
    plt.show()
else:
    print("⚠️ Aucun tweet trouvé pour ce terme.")