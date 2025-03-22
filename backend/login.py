from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

# Função para conectar ao SQL Server
def get_db_connection():
    conn = pyodbc.connect(
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=DESKTOP-O0GN42N;'
        'Database=DBCOMPRA;'
        'UID=adm;'
        'PWD=123'
    )
    return conn

# Rota para autenticar o login
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Conectar ao SQL Server
    conn = get_db_connection()
    cursor = conn.cursor()

    # Consulta para verificar o nome de usuário e a senha
    cursor.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()

    # Fechar a conexão com o banco
    conn.close()

    if user:
        return jsonify({"message": "Login bem-sucedido!"}), 200
    else:
        return jsonify({"message": "Usuário ou senha incorretos!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
