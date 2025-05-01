from flask import Flask, jsonify
from trend_chat import get_google_trends, get_twitter_trends, gerar_mensagens

app = Flask(__name__)

@app.route("/api/trends", methods=["GET"])
def trends():
    google = get_google_trends()
    twitter = get_twitter_trends()
    mensagens = gerar_mensagens(google, twitter)
    return jsonify({"google": google, "twitter": twitter, "mensagens": mensagens})

if __name__ == "__main__":
    app.run()
