import sys
from flask import Flask, render_template, send_from_directory
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)
app.config['FREEZER_BASE_URL'] = 'https://kwirtz.github.io/my_website/'  # Replace with your GitHub Pages URL
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FLATPAGES_AUTO_RELOAD'] = True
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_ROOT'] = 'posts'

pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/download_cv')
def download_cv():
    # Specify the path to your PDF file
    pdf_path = 'static/pdfs/cv_industry_kevin.pdf'
    
    # Return the file for download
    return send_from_directory('static/pdfs', 'cv_industry_kevin.pdf', as_attachment=True)

@app.route('/research_papers')
def research_papers():
    return render_template('research_papers.html')

@app.route('/teachings')
def teachings():
    return render_template('teachings.html')

@app.route('/blogposts')
def blogposts():
    return render_template('blogposts.html', posts=pages)

@app.route('/post_<int:post_id>')
def blogpost(post_id):
    post = next((p for p in pages if p.meta.get('id') == post_id), None)
    if post:
        return render_template('post.html', post=post)

@freezer.register_generator
def blogpost():
    for post in pages:
        yield {'post_id': post.meta.get('id')}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True)