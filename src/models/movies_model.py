from src.configs.database import db


class MoviesModel(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    studios = db.Column(db.String(255), nullable=False)
    producers = db.Column(db.String(255), nullable=False)
    winner = db.Column(db.Boolean, default=False)