import json
class NetworkIngredient:  # этот класс не связан с таблицами
    def __init__(self, id_i: int, title: str, category: str):
        self.id_i = id_i
        self.title = title
        self.category = category

    def to_json(self):  # просто селф, т.к. мы УЖЕ внутри класса NetworkIngredient
        data = json.dumps(self.__dict__)  # дикт возвращает все по ключам
        return data
