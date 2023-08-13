# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/age/', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if 0 < int(age) < 140:
            return f'Ваш возраст {age}'
        return 'Возраст введен неверно'
    return render_template('age.html')

if __name__ == '__main__':
    app.run(debug=True)
