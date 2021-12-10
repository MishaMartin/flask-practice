from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)

bookmarks = []
app.config['SECRET_KEY'] = 'w\x92@\xf9g\xe3\xc5u\xf8\x00\xf6\xc2T\x0e\xc8\xa7\xcc\x92\xbe8\xef\xf5\x80\xef'
def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = "misha",
        date = datetime.utcnow()
    ))

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def initials(self):
        return "{}. {}.".format(self.firstname[0], self.lastname[0])

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Title passed from view to template", user=User("Misha", "Martin"))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        flash("Stored bookmark '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html', user=User("Misha", "Martin"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__=='__main__':
    app.run(debug=True)