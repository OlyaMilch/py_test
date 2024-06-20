from main import db


class Recipe(db.Model):
    """
    Create database
    """

    id_r = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)

    # Упрощаем читаемость кода
    def __repr__(self):
        return f'<Recipe {self.title}'
