from flask import jsonify, request, Flask
from main import app
from flask_sqlalchemy import SQLAlchemy  # конструктор приложений
from main import db


# Определяем модель базы данных (в каком столбе какой тип данных)

class Recipe(db.Model):
    id_r = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)

    # Упрощаем читаемость кода
    def __repr__(self):
        return f'<Recipe {self.title}'


#  Получаем информацию по рецептам
@app.route('/recipes', methods=['GET'])  # Смотрим весь список
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify(
        [{'id_r': recipe.id_r, 'title': recipe.title, 'description': recipe.description} for recipe in
         recipes]), 200


# Получаем информацию по айди (здесь id_r, чтобы не конфликтовал с id ингредиентов)
@app.route('/recipe/<int:id_r>', methods=['GET'])
def get_recipe_by_id(id_r: int):
    recipe = Recipe.query.get(id_r)
    if recipe == None:
        return "Рецепт не найден"
    else:
        return jsonify(
            {'id_i': recipe.id_r, 'title': recipe.title, 'description': recipe.description}), 200


# Добавляем новую запись (требуется название и категория ингредиента, айди само поставится по порядку)
@app.route('/recipe', methods=['POST'])
def create_recipe():
    data = request.json
    new_recipe = Recipe(title=data['title'], category=data['category'])
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({'id_r': new_recipe.id_r, 'title': new_recipe.title, 'description': new_recipe.category}), 200


# удаление информации о рецепте
@app.route('/recipe/<int:id_r>', methods=['DELETE'])
def delete_recipe(id_r: int):
    try:
        recipe = Recipe.query.get(id_r)  # query - запрос
        db.session.delete(recipe)  # удаление всей записи по id
        db.session.commit()
    except Exception:
        return "Рецепт не найден"
