# Importando o módulo psycopg2, que é uma biblioteca Python para interagir com o banco de dados PostgreSQL
import psycopg2

# Definindo uma função para obter uma conexão com o banco de dados
def get_db_connection():
    # Criando uma conexão com o banco de dados usando psycopg2.connect e fornecendo os detalhes necessários
    conn = psycopg2.connect(
        host="localhost",  # O endereço do servidor do banco de dados, neste caso, é a máquina local
        database="postgres",  # O nome do banco de dados ao qual se conectar
        user="postgres",  # O nome do usuário para se conectar ao banco de dados
        password="12345"  # A senha do usuário para se conectar ao banco de dados
    )
    # Retornando a conexão criada
    return conn
