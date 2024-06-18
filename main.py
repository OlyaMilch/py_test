import os  # библиотека, позволяет работать с системой и файлам
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # путь к базе данных
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # отключаем предупреждения об изменения от Фласк
db = SQLAlchemy(app)

from ingredients import *
from recipes import *
from RecipeStep import *

if __name__ == "__main__":
    with app.app_context():  # с with дали контекст для create_all
        db.create_all()  # создаем бд, если ее нет
    app.run(debug=True)  # пока тру, т.к. надо видеть ошибки. Потом сменить на фолс, чтобы клиенты их не видели
