import json


class NetworkRecipe:  # этот класс не связан с таблицами
    def __init__(self, id: int, title: str, description: str):
        self.id = id
        self.title = title
        self.description = description

    def to_json(self):  # просто селф, т.к. мы УЖЕ внутри класса NetworkIngredient
        data = json.dumps(self.__dict__)  # дикт возвращает все по ключам
        return data
