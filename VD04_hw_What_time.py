from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    # Получаем текущие дату и время
    now = datetime.now()
    # Форматируем дату и время в строку
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # Возвращаем их в виде HTML-страницы
    return f"<h1>Текущие дата и время: {current_time}</h1>"


# Делаем запуск. Прописываем условие проверки
if __name__ == "__main__":
    app.run()
