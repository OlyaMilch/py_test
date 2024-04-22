import os  # библиотека, позволяет работать с системой и файлам
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

dirname = os.path.dirname(__file__)  # ищем  путь

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # путь к базе данных
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # отключаем предупреждения об изменения от Фласк
db = SQLAlchemy(app)

from ingredients import *

if __name__ == "__main__":
    app.run(debug=True)  # пока тру, т.к. надо видеть ошибки. Потом сменить на фолс, чтобы клиенты их не видели
