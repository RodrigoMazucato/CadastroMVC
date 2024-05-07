from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from model import User

@app.route('/')
def redicionar():
    return redirect('/cadastro')


@app.route('/cadastro', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('view.html')
    if request.method == 'POST':
        nome = request.form.get('nome')
        idade = request.form.get('idade')
        user = User(nome, idade)
        return redirect(url_for('listar'))

@app.route('/mostrar')
def listar():
   return render_template('listar.html')

app.run(debug=True)