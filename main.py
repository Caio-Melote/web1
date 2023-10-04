# main.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import psycopg2
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuração do CORS
#O CORS (Cross-Origin Resource Sharing) é um mecanismo que usa cabeçalhos HTTP adicionais para informar a um navegador que permita que um aplicativo Web 
# seja executado em uma origem (domínio) com permissão para acessar recursos selecionados de um servidor em uma origem distinta.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite requisições de todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos HTTP
)

@app.get("/chaves_disp")
def listar_chaves_disponiveis():
    try:
        # Conecta ao banco de dados PostgreSQL
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="12345"
        )
        
        # Cria um cursor para executar consultas SQL
        cur = conn.cursor()
        
        # Executa uma consulta para buscar as chaves disponíveis
        cur.execute("SELECT * FROM chaves WHERE status = 'disponivel'")
        
        # Recupera as chaves disponíveis do resultado da consulta
        chaves = cur.fetchall()
        
        # Fecha a conexão com o banco de dados
        cur.close()
        conn.close()
        
        # Retorna as chaves disponíveis como resposta
        return JSONResponse(content={"chaves": chaves})
    
    except (Exception, psycopg2.Error) as error:
        # Em caso de erro, retorna o erro como resposta
        return JSONResponse(content={"error": str(error)})