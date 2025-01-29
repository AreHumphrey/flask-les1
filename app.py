from flask import Flask, render_template, request, redirect, url_for
from models import db, Movie

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        review = request.form['review']
        rating = request.form['rating']

        new_movie = Movie(title=title, genre=genre, review=review, rating=int(rating))
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_movie.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
