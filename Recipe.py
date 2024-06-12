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
    network_recipe = [
        RecipeToNetworkRecipeMapper.map(recipe).__dict__  # дикт для вывода всех данных
        for recipe in recipes
    ]  # перебрали элементы, смаппили их и в json перевели
    return json.dumps(network_recipe), 200  # вывод на одной строке в браузере благодаря json


@app.route('/recipe/<int:id_r>', methods=['GET'])
def get_recipe_by_id(id_r: int):
    """
    Getting information by id
    """

    recipe = Recipe.query.get(id_r)
    if recipe is None:  # сначала проверка, потом маппер
        return 'Recipe not found'
    else:
        network_recipe = RecipeToNetworkRecipeMapper.map(recipe)
        return network_recipe.to_json(), 200


@app.route('/recipe', methods=['POST'])
def create_recipe():
    """
    Adding an entry about a new ingredient
    """

    data = request.json
    new_recipe = Recipe(title=data['title'], category=data['category'])
    db.session.add(new_recipe)
    db.session.commit()
    network_recipe = RecipeToNetworkRecipeMapper.map(new_recipe)
    return network_recipe.to_json(), 200


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


from class_NetworkRecipe import *
from class_RecipeToNetworkRecipeMapper import *
