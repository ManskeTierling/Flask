from os import name
import re
from flask import Flask, render_template, redirect, request
from repositorio import insert, conexao, select, select_id, delete, update

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
    return redirect('/listar/todos')

@app.route('/listar/todos', methods=['get'])
def listar():
    db = conexao()
    lista_banco = select(db)
    return render_template('listar.html',lista_banco = lista_banco)

@app.route('/listar/<int:id>/', methods=['get'])
def listar_por_id(id):
    db = conexao()
    registro = select_id(db, id)
    return render_template('listar_id.html',lista_banco = registro)

@app.route('/delete', methods=['get'])
def deletar():
    id = request.args['id']
    db = conexao()
    delete(db, id)
    return redirect('/listar/todos')

@app.route('/alterar', methods=['get'])
def alterar():
    id = request.args['id']
    db = conexao()
    registro = select_id(db, id)
    return render_template('listar_id.html', id = registro[0], nome=registro[1],
    sobrenome = registro[2], cpf = registro[3], email = registro[4],
    telefone = registro[5])

@app.route('/alterar/salvar', methods=['post'])
def alterar_salvar():
    id = request.form['id']
    nome = request.form['name']
    sobrenome = request.form['last_name']
    cpf = request.form['cpf']
    email = request.form['email']
    telefone = request.form['phone']
    db = conexao()
    update(db, id, nome, sobrenome, cpf, email, telefone)
    return redirect('/listar/todos')

app.run(debug=True)