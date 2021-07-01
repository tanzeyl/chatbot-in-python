from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot =  ChatBot('Chatterbot',
             logic_adapters = [
                 {
                     'import_path': 'chatterbot.logic.BestMatch',
                     'default_response': 'I am sorry, I do not understand. I am still learning. Please contact ktanzeel80@gmail.com for further assistance.',
                     'maximum_similarity_threshold': 0.90
                 }
             ],
             read_only = True,
             preprocessors=['chatterbot.preprocessors.clean_whitespace',
'chatterbot.preprocessors.unescape_html',
'chatterbot.preprocessors.convert_to_ascii'])
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get",methods=['GET'])
def get_bot_response():
    userText = request.args.get("msg")
    return str(english_bot.get_response(userText))

if __name__ == "__main__":
    app.run(debug = True)