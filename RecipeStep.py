from flask import jsonify, request
from main import app
from main import db


# Определяем модель базы данных (в каком столбе какой тип данных)

class RecipeStep(db.Model):
    id_s = db.Column(db.Integer, unique=True, primary_key=True)  # ты хочешь id в str, но точно ли нам это надо?
    next_step = db.Column(db.Integer, unique=False, nullable=False)
    prev_step = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)

    # Упрощаем читаемость кода
    def __repr__(self):
        return f'<Recipe_step {self.title}'


#  Получаем информацию по рецептам
@app.route('/rs', methods=['GET'])  # Смотрим весь список
def get_recipe_steps():
    rs = RecipeStep.query.all()
    return jsonify(
        [{'id_s': i.id_s, 'next_step': i.next_step, 'prev_step': i.prev_step, 'description': i.description} for i in
         rs]), 200


# Получаем информацию по айди
@app.route('/step/<int:id_s>', methods=['GET'])
def get_recipe_by_id_s(id_s: int):
    rs = RecipeStep.query.get(id_s)
    if rs is None:
        return "Рецепт не найден"
    else:
        return jsonify(
            {'id_s': rs.id_s, 'next_step': rs.next_step, 'prev_step': rs.prev_step, 'description': rs.description}), 200


# Добавляем новую запись
@app.route('/step', methods=['POST'])
def create_recipe_step():
    data = request.json
    new_rs = RecipeStep(description=data['description'], prev_step=data['prev_step'], next_step=data['next_step'])
    db.session.add(new_rs)
    db.session.commit()
    return jsonify({'id_s': new_rs.id_s, 'next_step': new_rs.next_step, 'prev_step': new_rs.prev_step,
                    'description': new_rs.description}), 200


# удаление информации о рецепте
@app.route('/step/<int:id_s>', methods=['DELETE'])
def delete_recipe_step(id_s: int):
    try:
        rs = RecipeStep.query.get(id_s)  # query - запрос
        db.session.delete(rs)  # удаление всей записи по id
        db.session.commit()
    except Exception:
        return "Рецепт не найден"
