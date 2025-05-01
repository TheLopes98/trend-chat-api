import tweepy
from pytrends.request import TrendReq
import os

def get_google_trends():
    try:
        pytrends = TrendReq(hl='pt-BR', tz=180)
        termos = ['Futebol', 'Celebridades', 'Música', 'Política', 'Novelas']
        pytrends.build_payload(kw_list=termos, timeframe='now 7-d', geo='BR')
        dados = pytrends.interest_over_time()

        if dados.empty:
            return []

        maiores = dados[termos].mean().sort_values(ascending=False).head(3)
        return list(maiores.index)
    except Exception as e:
        print("Erro ao buscar trends do Google:", e)
        return []

def get_twitter_trends():
    BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

    try:
        client = tweepy.Client(bearer_token=BEARER_TOKEN)
        query = '#BBB OR #Funk OR #TBT OR #Brasil -is:retweet lang:pt'
        tweets = client.search_recent_tweets(query=query, max_results=10)

        if tweets.data is None:
            return []

        hashtags = []
        for tweet in tweets.data:
            hashtags.extend([word.lower() for word in tweet.text.split() if word.startswith('#')])
        return list(set(hashtags))[:5]
    except Exception as e:
        print("Erro ao buscar trends do Twitter:", e)
        return []

def gerar_mensagens(trends_google, trends_twitter):
    mensagens = []
    for tg in trends_google:
        mensagens.append(f"Hoje o Brasil só fala de {tg}... mas eu prefiro falar com você 😏")
    for tt in trends_twitter:
        mensagens.append(f"Vi que {tt} tá bombando... e a gente aqui sem assunto? Bora mudar isso!")
    if not mensagens:
        mensagens.append("Nem o Google nem o Twitter têm algo mais interessante que você hoje 😎")
    return mensagens
