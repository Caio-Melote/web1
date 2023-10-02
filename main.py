# main.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import psycopg2

app = FastAPI()

@app.get("/chaves")
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
        return JSONResponse(content={"error": str(error)})