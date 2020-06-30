import random
from datetime import datetime
from flask import Flask
app = Flask(__name__)

random.seed(datetime.now())

@app.route('/')
def fighter():
    return 'Fighters Ready!'