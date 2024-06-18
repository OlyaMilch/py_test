from networkingredient import NetworkIngredient
from ingredients import Ingredient


class IngredientToNetworkIngredientMapper:
    @classmethod  # не cоздаем объект от класса, а вызываем объект от класса
    def map(cls, ingredient: Ingredient):  # cls-обозначает класс, а не объект
        return NetworkIngredient(ingredient.id_i, ingredient.title, ingredient.category)  # возвращает созданный объект