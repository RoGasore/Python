from TikTokApi import TikTokApi
import pandas as pd 
import schedule
import os
import time 
from datetime import datetime

hashtags = ["Goma", 
            "RDC", 
            "NordKivu", 
            "Virunga", 
            "Congo", 
            "masisi", 
            "mushaki", 
            "vacation",
            "nature"
            "travel"
            "tourism"
            "congolese"
            "congolais"
            "congotourism"
            "congotravel"
            ] 

csv_file = "tiktok_data.csv"

def collect_data() : 
    print(f"[{datetime.now()}] : Debut de la collecte...")
    data = []
    api = TikTokApi()  # Correction ici
    for tag in hashtags: 
        try : 
            videos = api.hashtags(name=tag).videos(count=20)
            for video in videos : 
                data.append({
                    "hashtag" : tag,
                    "auteur" : video.author.username,
                    "description" : video.desc,
                    "likes" : video.stats["diggCount"],
                    "shares" : video.stats["shareCount"],
                    "commentaires" : video.stats["commentCount"],
                    "date_publication" : datetime.fromtimestamp(video.create_time),
                    "video_url" : f"https://www.tiktok.com/@{video.author.username}/video/{video.id}"
                })
        except Exception as e :
            print(f"Erreur sur le hashtag {tag} : {e}")          

    df = pd.DataFrame(data)
    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode = 'a', header = False, index = False)
    else : 
        df.to_csv(csv_file, index = False)
    print(f"[{datetime.now()}] Collecte terminée. {len(data)} videos ajoutées.")


def auto_commit() : 
    os.system('git add .')
    os.system('git commit -m "mis à jour"')
    os.system('git push')
    print(f"{[datetime.now()]} Commit auto effectué")

def joob():
    collect_data()
    auto_commit()

schedule.every(1).minutes.do(joob)

print("Le collecteur TikTok tourne.... Ctrl + C pour arreter")
while True :
    schedule.run_pending()
    time.sleep(1)
