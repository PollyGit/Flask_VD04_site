#Импортируем класс Flask из модуля
from flask import Flask, render_template

#Создаём переменную и сохраняем в неё объект класса Flask
#спец пременная __name__, помогает находить имя текущего модуля
app = Flask(__name__)

#Начинаем создавать функции.
# Используем декоратор из модуля Flask:
#route — конкретный декоратор, чтобы позже прописать URL-адрес страницы.
@app.route("/")
def main_page():
    return render_template("index_VD04_hw.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts_VD04_hw.html")

@app.route("/blog/")
def blog():
    return render_template("blog_VD04_hw.html")

#Делаем запуск. Прописываем условие проверки
if __name__ == "__main__":
    app.run()