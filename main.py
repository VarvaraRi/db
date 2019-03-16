from flask import Flask, redirect, render_template, session
from login import LoginForm
from add_drug import AddDrugForm
from db import DB
from user import UserModel
from drug import DrugModel
from basket import BasketModel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db = DB()

def exits(args):
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user_model = UserModel(db.get_connection())
        exists = user_model.exists(user_name, password)
        if (exists[0]):
            session['username'] = user_name
            session['user_id'] = exists[1]
        return redirect("/index")
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/add_drug', methods=['GET', 'POST'])
def add_news():
    if 'username' not in session:
        return redirect('/login')
    if session['username'] != 'admin':
        return redirect('/login')
    form = AddDrugForm()
    if form.validate_on_submit():
        name = form.name.data
        discription = form.discript.data
        number = form.number.data
        dm = DrugModel(db.get_connection())
        dm.insert(name,discription,number,session['user_id'])
        return redirect("/index")
    return render_template('add_drug.html', title='Добавление товара', form=form, username=session['username'])


@app.route('/delete_drug/<int:drug_id>', methods=['GET'])
def delete_news(drug_id):
    if 'username' not in session:
        return redirect('/login')
    if session['username'] != 'admin':
        return redirect('/login')
    dm = DrugModel(db.get_connection())
    dm.delete(drug_id)
    return redirect("/index")


@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        name = session['username']
    else:
        name = 'Вход'
    dm = DrugModel(db.get_connection()).get_all()
    drug = []
    for i in dm:
        if int(i[3]) > 0:
            drug.append(i)
    return render_template('index.html', username=name, news=drug)


@app.route('/basket', methods = ['GET', 'POST'])
def basket():
    if 'username' not in session:
        return redirect('/login')
    basket = BasketModel(db.get_connection()).get_all(session['user_id'])
    drug = DrugModel(db.get_connection())
    bask = []
    for i in basket:
        bask.append(drug.get(i[1]))
    return render_template('basket.html', username=session['username'], news=bask)


@app.route('/error', methods=['GET', 'POST'])
def error():
    return "error, unknown user"


@app.route('/logout')
def logout():
    session.pop('username',0)
    session.pop('user_id',0)
    return redirect('/login')

@app.route('/signin',  methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user_model = UserModel(db.get_connection())
        user_model.insert(user_name, password)
        return redirect('/login')
    return render_template('sign_in.html', title='Регестрация', form=form)


@app.route('/addbasket/<int:drug_id>', methods=['GET'])
def addbasket(drug_id):
    if 'username' not in session:
        return redirect('/login')
    bm = BasketModel(db.get_connection())
    bm.insert(drug_id, session['user_id'])
    drug = DrugModel(db.get_connection())
    drug.update(drug_id)
    return redirect("/index")


@app.route('/delete_basket/<int:drug_id>', methods=['GET'])
def delete_basket(drug_id):
    if 'username' not in session:
        return redirect('/login')
    bask = BasketModel(db.get_connection())
    bask.delete(drug_id, session['user_id'])
    drug = DrugModel(db.get_connection())
    drug.update(drug_id, -1)
    return redirect('/basket')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)