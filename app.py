from flask import Flask, render_template
## From: https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')
