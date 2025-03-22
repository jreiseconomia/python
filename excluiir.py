import pyodbc

# Defina as informações de conexão (ajuste conforme necessário)
conn = pyodbc.connect(
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=DESKTOP-O0GN42N;'
        'Database=DBCOMPRA;'
        'UID=adm;'
        'PWD=12345678'
    )

# Crie um cursor
cursor = conn.cursor()

# Defina a consulta SQL para selecionar todos os dados de uma tabela
query = "SELECT * FROM Usuarios"

# Execute a consulta
cursor.execute(query)

# Imprima os resultados
columns = [column[0] for column in cursor.description]  # Nome das colunas
print("\t".join(columns))  # Imprime os nomes das colunas
print("-" * 50)  # Linha para separar os títulos das linhas

for row in cursor.fetchall():
    print("\t".join(str(value) for value in row))  # Imprime os valores das linhas

# Feche a conexão
cursor.close()
conn.close()
