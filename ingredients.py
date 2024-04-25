from flask import jsonify, request, Flask
from flask_sqlalchemy import SQLAlchemy
from main import app
from main import db


# Определяем модель базы данных (в каком столбе какой тип данных)

class Ingredient(db.Model):
    id_i = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    category = db.Column(db.String(120), unique=False, nullable=False)

    # Упрощаем читаемость кода
    def __repr__(self):
        return f'<Ingredient {self.title}'


#  Получаем информацию по ингредиенту
@app.route('/ingredients', methods=['GET'])  # Смотрим весь список
def get_ingredient():
    ingredients = Ingredient.query.all()
    return jsonify(
        [{'id_i': Ingredient.id_i, 'username': Ingredient.title, 'category': Ingredient.category} for Ingr in
         ingredients])


# Получаем информацию по айди
@app.route('/id_i/<int:id_i>', methods=['GET'])
def get_id_ingredient(id_i):
    ingredient = Ingredient.query.get(id_i)
    return jsonify(ingredient)


# Добавляем новую запись (требуется название и категория ингредиента, айди само поставится по порядку)
@app.route('/ingredient', methods=['POST'])
def create_ingredient():
    data = request.json
    new_ingredient = Ingredient(title=data['title'], category=data['category'])
    db.session.add(new_ingredient)
    db.session.commit()
    return jsonify(
        {'id_i': new_ingredient.id_i, 'title': new_ingredient.title, 'category': new_ingredient.category}), 201


# удаление информации о ингредиенте
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_recipe(id_i: int):
    try:
        ingredient = Ingredient.query.get(id_i)  # query - запрос
        db.session.delete(ingredient)  # удаление всей записи по id
        db.session.commit()
    except Exception:
        return "Ингредиент не найден"
