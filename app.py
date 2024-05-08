from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from model import User, Base
from flask_migrate import Migrate



db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)
migrate = Migrate(app, db)
 
 
@app.get('/')
@app.get('/cadastro')
def index_get():
    return render_template('view.html')


@app.post('/cadastro')
def index_post():
    nome = request.form.get('nome')
    idade = request.form.get('idade')
    user = User(nome=nome, idade=idade)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('listar'))

@app.route('/mostrar')
def listar():
   return render_template('listar.html')


if __name__ == '__main__':
    app.run(debug=True)