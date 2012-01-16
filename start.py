from flask import Flask
from flask.helpers import jsonify
import simplejson
from flask.templating import render_template
import tasks

app = Flask(__name__)

@app.route('/tasks/')
def prepare_tasks():
    result = tasks.get_task()
    print result
    return simplejson.dumps({"result": result})

@app.route("/")
def hello():
    return render_template('dash.html', tasks=tasks.get_task())

if __name__ == "__main__":
    app.run(debug=True)