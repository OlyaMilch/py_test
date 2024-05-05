from flask import jsonify, request
from main import app
from main import db


# Определяем модель базы данных (в каком столбе какой тип данных)

class Recipe_step(db.Model):
    id_s = db.Column(db.Integer, unique=True, primary_key=True)  # ты хочешь id в str, но точно ли нам это надо?
    nextStep = db.Column(db.String(80), unique=False, nullable=False)
    prevStep = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)

    # Упрощаем читаемость кода
    def __repr__(self):
        return f'<Recipe_step {self.title}'


#  Получаем информацию по рецептам
@app.route('/rs', methods=['GET'])  # Смотрим весь список
def get_recipe_steps():
    rs = Recipe_step.query.all()
    return jsonify(
        [{'id_s': rs.id_s, 'nextStep': rs.nextStep, 'prevStep': rs.prevStep, 'description': rs.description} for rs in
         rs]), 200


# перебор на 25-26 строке сработает или нет?


# Получаем информацию по айди
@app.route('/step/<int:id_s>', methods=['GET'])
def get_recipe_by_id_s(id_s: int):
    rs = Recipe_step.query.get(id_s)
    if rs is None:
        return "Рецепт не найден"
    else:
        return jsonify(
            {'id_s': rs.id_s, 'nextStep': rs.nextStep, 'prevStep': rs.prevStep, 'description': rs.description}), 200


# Добавляем новую запись
@app.route('/step', methods=['POST'])
def create_recipe_step():
    data = request.json
    new_rs = Recipe_step(description=data['description'], prevStep=data['prevStep'], nextStep=data['nextStep'])
    db.session.add(new_rs)
    db.session.commit()
    return jsonify({'id_s': new_rs.id_s, 'nextStep': new_rs.nextStep, 'prevStep': new_rs.prevStep,
                    'description': new_rs.description}), 200


# на 45 строке нужно ли оставить шаги?

# удаление информации о рецепте
@app.route('/step/<int:id_s>', methods=['DELETE'])
def delete_recipe_step(id_s: int):
    try:
        rs = Recipe_step.query.get(id_s)  # query - запрос
        db.session.delete(rs)  # удаление всей записи по id
        db.session.commit()
    except Exception:
        return "Рецепт не найден"
