from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    genre = db.Column(db.String(50), nullable=False)

    review = db.Column(db.Text, nullable=False)

    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Фильм {self.title}>'
