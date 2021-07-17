from os import name
from flask import Flask, render_template, redirect, request
from repositorio import insert, conexao

app = Flask(__name__)

@app.route('/', methods=['get'])
def pagina_inicial():
    return render_template('index.html')

@app.route('/cadastro',methods=['get'])
def cadastro():
    return render_template('cadastros.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['name']
    sobrenome = request.form['last_name']
    cpf = request.form['cpf']
    email = request.form['email']
    fone = request.form['phone']
    db = conexao()
    insert(db, nome, sobrenome, cpf, email, fone)

    return redirect('/cadastro')

app.run(debug=True)