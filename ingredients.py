from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy  # конструктор приложений

from main import db
from main import app

# Определяем модель базы данных (в каком столбе какой тип данных)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=False)
    title = db.Column(db.String(80), unique=True, nullable=False)
    category = db.Column(db.String(120), unique=True, nullable=False)

    # Упрощаем читаемость кода
    def __repr__(self):
        return '<Ingredient %r>' % self.title


#  Получаем информацию по ингредиенту
@app.route('/ingredients', methods=['GET'])  # Смотрим весь список
def get_users():
    ingredients = Ingredient.query.all()
    return jsonify(
        [{'id': Ingredient.id, 'username': Ingredient.title, 'category': Ingredient.category} for Ingr in
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
    new_ingredient = Ingredient(title=data['title'], category=data['category'])
    db.session.add(new_ingredient)
    db.session.commit()
    return jsonify({'id': new_ingredient.id, 'title': new_ingredient.title, 'category': new_ingredient.category}), 201
