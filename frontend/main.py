from flask import Flask, render_template, jsonify
from summarization.SummaryService import summarizedTextStore
from flaskwebgui import FlaskUI
import threading

app = Flask(__name__)
ui = FlaskUI(app, width=500, height=800)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/summary_content")
def getSummaryContent():
    return jsonify(summarizedTextStore)

def renderGUI():
    guiThread = threading.Thread(target=ui.run, daemon=True)
    guiThread.start()

# if __name__ == "__main__":
#     ui.run(debug=True)
