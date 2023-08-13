# Создать страницу, на которой будет форма для ввода имени и электронной почты, 
# при отправке которой будет создан cookie-файл с данными пользователя, а также 
# будет произведено перенаправление на страницу приветствия, где будет отображаться 
# имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет 
# удалён cookie-файл с данными пользователя и произведено перенаправление на 
# страницу ввода имени и электронной почты.

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, make_response

app = Flask(__name__)
app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

@app.route('/')
def main():
    return render_template('username.html')
    
@app.route('/enter/', methods=['GET', 'POST'])
def enter():
    name = request.form['name']
    email = request.form['email']
    response = make_response(redirect('/greet')) 
    response.set_cookie('username', name)
    response.set_cookie('useremail', email)
    return response

@app.route('/greet')
def greet():
    username = request.cookies.get('username')
    if username:
        return render_template('greeting.html')
    return redirect('/')

@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('username')
    response.delete_cookie('useremail')
    return response


if __name__ == '__main__':
    app.run(debug=True)
