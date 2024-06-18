from flask import request
from Ingredient import Ingredient
from main import app
from main import db
import json
from ingredientmapper import IngredientToNetworkIngredientMapper


@app.route('/ingredients', methods=['GET'])  # Смотрим весь список
def get_ingredients():
    """
    Getting information by ingredient
    """

    ingredients = Ingredient.query.all()
    network_ingredient = [
        IngredientToNetworkIngredientMapper.map(ingredient).__dict__  # без дикта не очень красивый вывод
        for ingredient in ingredients
    ]  # перебрали элементы, смаппили их и в json перевели
    return json.dumps(network_ingredient), 200  # вывод на одной строке в браузере благодаря json


@app.route('/ingredient/<int:id_i>', methods=['GET'])
def get_ingredient_by_id(id_i):
    """
    Getting information by id
    """

    ingredient = Ingredient.query.get(id_i)
    if ingredient is None:  # сначала проверка, потом маппер
        return 'Ingredient not found'
    network_ingredient = IngredientToNetworkIngredientMapper.map(ingredient)
    return network_ingredient.to_json(), 200


@app.route('/ingredient', methods=['POST'])
def create_ingredient():
    data = request.json
    new_ingredient = Ingredient(title=data['title'], category=data['category'])
    db.session.add(new_ingredient)
    db.session.commit()
    network_ingredient = IngredientToNetworkIngredientMapper.map(new_ingredient)
    return network_ingredient.to_json(), 200


@app.route('/recipe/<int:id>', methods=['DELETE'])
def delete_ingredient(id_i: int):
    """
    Removing ingredient information
    """

    try:
        ingredient = Ingredient.query.get(id_i)  # query - запрос
        db.session.delete(ingredient)  # удаление всей записи по id
        db.session.commit()
    except Exception:
        return "Ingredient not found"
