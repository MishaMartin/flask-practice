from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash

# from forms import BookmarkForm

app = Flask(__name__)

bookmarks = []
app.config['SECRET_KEY'] = 'w\x92@\xf9g\xe3\xc5u\xf8\x00\xf6\xc2T\x0e\xc8\xa7\xcc\x92\xbe8\xef\xf5\x80\xef'
def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = "misha",
        date = datetime.utcnow()
    ))

def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]
class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def initials(self):
        return "{}. {}.".format(self.firstname[0], self.lastname[0])

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Title passed from view to template", user=User("Misha", "Martin"), new_bookmark=new_bookmarks(5))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        store_bookmark(url, description)
        flash("Stored '{}'",format(description))
        return redirect(url_for('index'))
    return render_template('add.html',form=form, user=User("Misha", "Martin"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__=='__main__':
    app.run(debug=True)