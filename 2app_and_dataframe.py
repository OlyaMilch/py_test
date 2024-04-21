from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy  # конструктор приложений

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # путь к базе данных
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # отключаем предупреждения об изменения от Фласк
db = SQLAlchemy(app)


# Определяем модель базы данных (в каком столбе какой тип данных)
class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    category = db.Column(db.String(120), unique=True, nullable=False)

    # Упрощение читаемости файла
    def __repr__(self):
        return '<Ingredient %r>' % self.title


#  Получаем информацию по ингредиенту
@app.route('/ingredients', methods=['GET'])  # Вот здесь он недоволен
def get_users():
    ingredients = ingredient.query.all()
    return jsonify(
        [{'id': ingredient.id, 'username': ingredient.title, 'category': ingredient.category} for ingr in
         ingredients])


# Получаем информацию по айди
@app.route('/id', methods=['GET'])
def get_id_ingredients():
    db.create_all()
    return ""


# Добавляем новую запись (требуется название и категория ингредиента, айди само поставится по порядку)
@app.route('/ingredient', methods=['POST'])
def create_ingredient():
    data = request.json
    new_ingredient = ingredient(title=data['title'], category=data['category'])
    db.session.add(new_ingredient)
    db.session.commit()
    return jsonify({'id': new_ingredient.id, 'title': new_ingredient.title, 'category': new_ingredient.category}), 201


if __name__ == '__main__':
    app.run(debug=True)
