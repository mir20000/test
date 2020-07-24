from flask import Flask

app = Flask(__name__)

@app.route('/formapp/<latitude>/<longitude>')
def index(latitude,longitude):
    return '<h1>your input<br><br> latitude=> {} <br> longitude=> {}</h1>'.format(latitude,longitude)