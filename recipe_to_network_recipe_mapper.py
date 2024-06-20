from recipes import Recipe
from network_recipe import NetworkRecipe


class RecipeToNetworkRecipeMapper:
    @classmethod  # не cоздаем объект от класса, а вызываем объект от класса
    def map(cls, recipe: Recipe):  # cls-обозначает класс, а не объект
        return NetworkRecipe(recipe.id_r, recipe.title, recipe.description)  # возвращает созданный объект
