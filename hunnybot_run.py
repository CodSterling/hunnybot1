import asyncio
import threading
from flask import Flask, request
import json
from hunnys import bot
from hunnys import on_ready

# Load configuration securely and handle exceptions
try:
    with open('token2.json') as config_file:
        config = json.load(config_file)
        token = config['token']
except (FileNotFoundError, KeyError):
    print("Error loading config file or reading the token")
    exit(1)

app = Flask(__name__)

# Assuming the bot class from 'maze' is relevant and properly defined
bot = bot

@app.route('/')
def index():
    return 'Welcome to my bot!'

@app.route('/chat', methods=['POST'])
def chat():
    channel_id = request.form.get('channel_id')
    if channel_id:
        channel = bot.get_channel(int(channel_id))
        if channel:
            asyncio.run(on_ready(channel))
            return "Event triggered successfully", 200
        else:
            return "Channel not found", 404
    else:
        return "No channel_id provided", 400

def run_flask():
    app.run(debug=True, use_reloader=False, threaded=True)

# define a function to run the actual bot (adjust as per actual bot logic and library)
def run_bot():
    # dummy function to represent the bot running
    import time
    while True:
        print("Bot is running...")
        time.sleep(10)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    bot_thread = threading.Thread(target=run_bot)

    flask_thread.start()
    bot_thread.start()