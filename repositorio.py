import mysql.connector


def conexao():
    db = mysql.connector.connect(
        host='localhost',
        database= 'CADASTRO',
        user='root',
        password='Blumenau1'
    )
    return db

def insert(db, nome, sobrenome, cpf, email, fone):
    comando_sql = 'INSERT INTO CONTATOS (NOME, SOBRENOME, CPF, EMAIL, TELEFONE) VALUES (%s, %s, %s, %s, %s)'
    parametros = (nome, sobrenome, cpf, email, fone)
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql, parametros)
        db.commit()
        cursor.close()
        print('Registro inserido com sucesso.')
    except Exception as error:
        print(error)
        