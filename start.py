from flask import Flask
import tasks

app = Flask(__name__)

@app.route("/")
def hello():
    return str(tasks.get_task()) or 'Problem'

if __name__ == "__main__":
    app.run()