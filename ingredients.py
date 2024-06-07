from flask import request
from main import app
from main import db
import json


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


class NetworkIngredient:  # этот класс не связан с таблицами
    def __init__(self, id_i: int, title: str, category: str):
        self.id_i = id_i
        self.title = title
        self.category = category

    def to_json(self):  # просто селф, т.к. мы УЖЕ внутри класса NetworkIngredient
        data = json.dumps(self.__dict__)  # дикт возвращает все по ключам
        return data


class IngredientToNetworkIngredientMapper:
    @classmethod  # не cоздаем объект от класса, а вызываем объект от класса
    def map(cls, ingredient: Ingredient):  # cls-обозначает класс, а не объект
        return NetworkIngredient(ingredient.id_i, ingredient.title, ingredient.category)  # возвращает созданный объект
