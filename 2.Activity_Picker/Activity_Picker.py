from flask import Flask, render_template
from random import randint

app = Flask(__name__)

action = [
    'sleep' , 'do homework' , 'eat' , 'play game' , 'video' , 'go out' , 
    'learn Engliah' , 'read novel' , 'practice coding' , 'cook' , 'shop'
    ]


@app.route('/')
def index():
    return render_template('index.html', action = action)

@app.route('/get')
def get():
    num = randint(0, len(action)-1)
    return render_template('index.html', action = action, h = action[num])


app.run(debug=True, port=52143)
