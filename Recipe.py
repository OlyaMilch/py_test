from flask import jsonify, request
from main import app
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


@app.route('/recipes', methods=['GET'])  # Смотрим весь список
def get_recipes():
    """
    Getting information by recipes
    """

    recipes = Recipe.query.all()
    return jsonify(
        [{'id_r': recipe.id_r, 'title': recipe.title, 'description': recipe.description} for recipe in
         recipes]), 200


@app.route('/recipe/<int:id_r>', methods=['GET'])
def get_recipe_by_id(id_r: int):
    """
    Getting information by id
    """

    recipe = Recipe.query.get(id_r)
    if recipe is None:
        return "Recipe not found"
    else:
        return jsonify(
            {'id_i': recipe.id_r, 'title': recipe.title, 'description': recipe.description}), 200


@app.route('/recipe', methods=['POST'])
def create_recipe():
    """
    Adding an entry about a new ingredient
    """

    data = request.json
    new_recipe = Recipe(title=data['title'], category=data['category'])
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({'id_r': new_recipe.id_r, 'title': new_recipe.title, 'description': new_recipe.category}), 200


@app.route('/recipe/<int:id_r>', methods=['DELETE'])
def delete_recipe(id_r: int):
    """
    Removing recipe information
    """

    try:
        recipe = Recipe.query.get(id_r)  # query - запрос
        db.session.delete(recipe)  # удаление всей записи по id
        db.session.commit()
    except Exception:
        return "Recipe not found"
