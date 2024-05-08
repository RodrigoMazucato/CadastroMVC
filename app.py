from flask import Flask, render_template, request, redirect, url_for
from model import db, User
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'

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
    user = User(nome, idade)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('listar'))

@app.get('/mostrar')
def listar():
    users = User.query.all()
    return render_template('listar.html', pessoas=users)

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)