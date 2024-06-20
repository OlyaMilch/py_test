from main import db


# Определяем модель базы данных (в каком столбе какой тип данных)
class Ingredient(db.Model):
    """
    Create database
    """

    id_i = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    category = db.Column(db.String(120), unique=False, nullable=False)

    # Упрощаем читаемость кода
    def __repr__(self):
        return f'<Ingredient {self.title}'