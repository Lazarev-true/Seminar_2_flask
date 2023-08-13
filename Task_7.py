# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/num/', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        num = float(request.form.get('num'))
        return f'Число {num}, квадрат этого числа {num ** 2}'
    return render_template('num.html')

if __name__ == '__main__':
    app.run(debug=True)
