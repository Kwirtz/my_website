import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/research_papers')
def research_papers():
    return render_template('research_papers.html')

@app.route('/teachings')
def teachings():
    return render_template('teachings.html')

@app.route('/blogposts')
def blogpost():
    return render_template('blogposts.html')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run()