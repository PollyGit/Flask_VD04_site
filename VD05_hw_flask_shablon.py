from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main_page():
    context = {
        'Title': 'Главная',
        "link": "Перейти в кинотеатр"
    }
    return render_template("home_VD05_hw.html", **context)


@app.route("/about/")
def blog():
    context = {
        'Title': 'Блог',
        "link": "Перейти в кинотеатр"
    }
    return render_template("about_VD05_hw.html", **context)


@app.route("/contacts/")
def contacts():
    context = {
        'Title': 'Контакты',
        "link": "Перейти в кинотеатр"
    }
    return render_template("contacts_VD05_hw.html", **context)


if __name__ == "__main__":
    app.run()
