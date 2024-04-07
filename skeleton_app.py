import pandas as pd
import os  # библиотека, позволяет работать с системой и файлам
from flask import Flask

dirname = os.path.dirname(__file__)  # ищем  путь
filepath = os.path.join(dirname, "Information.txt")  # делаем новый путь до файла
info = pd.read_csv(filepath, encoding='windows-1251')
print(info.head)

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/info")  # после слеша можем укзать слово, которое запускает app в браузере
def about():
    return info.to_csv()


if __name__ == "__main__":
    app.run(debug=True)  # пока тру, т.к. надо видеть ошибки. Потом сменить на фолс, чтобы клиенты их не видели
