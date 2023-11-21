# Importando as classes necessárias
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from database.connection import get_db_connection
from models.model_chave import Chave

# Criando um roteador de API
router = APIRouter()

# Definindo uma rota GET para "/chaves"
@router.get("/chaves")
def listar_chaves():
    try:
        # Obtendo a conexão com o banco de dados
        conn = get_db_connection()
        # Criando um cursor
        cur = conn.cursor()
        # Executando a consulta SQL para obter todas as chaves
        cur.execute("SELECT * FROM chaves WHERE status != 'inativo'")
        # Obtendo todos os resultados da consulta
        chaves = cur.fetchall()
        # Fechando o cursor e a conexão com o banco de dados
        cur.close()
        conn.close()
        # Retornando as chaves em uma resposta JSON
        return JSONResponse(content={"chaves": chaves})
    except (Exception, psycopg2.Error) as error:
        # Em caso de erro, retornar o erro em uma resposta JSON
        return JSONResponse(content={"error": str(error)})
    
# Definindo uma rota GET para "/chaves_disp"
@router.get("/chaves_disp")
def listar_chaves_disponiveis():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Executando a consulta SQL para obter todas as chaves disponíveis
        cur.execute("SELECT * FROM chaves WHERE status = 'disponivel'")
        chaves = cur.fetchall()
        cur.close()
        conn.close()
        return JSONResponse(content={"chaves": chaves})
    except (Exception, psycopg2.Error) as error:
        return JSONResponse(content={"error": str(error)})

# Definindo uma rota POST para "/chaves"
@router.post("/chaves")
def adicionar_chave(chave: Chave):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Executando a consulta SQL para inserir uma nova chave no banco de dados
        cur.execute("INSERT INTO chaves (nome, situacao, status) VALUES (%s, %s, %s)", (chave.nome, chave.situacao, chave.status))
        # Confirmando a transação
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Chave adicionada com sucesso!"}
    except (Exception, psycopg2.Error) as error:
        raise HTTPException(status_code=400, detail=str(error))

# Definindo uma rota DELETE para "/chaves"
@router.delete("/chaves/{id}")
def deletar_chave(id: int):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Verificando se a chave existe
        cur.execute("SELECT * FROM chaves WHERE id = %s", (id,))
        resultado = cur.fetchone()
        if resultado is None:
            return {"message": "Chave não encontrada!"}
        # Executando a consulta SQL para alterar o status da chave para 'inativo'
        cur.execute("UPDATE chaves SET status = 'inativo' WHERE id = %s", (id,))
        # Confirmando a transação
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Chave deletada com sucesso!"}
    except (Exception, psycopg2.Error) as error:
        raise HTTPException(status_code=400, detail=str(error))

# Definindo uma rota PUT para "/chaves"
@router.put("/chaves/{nome}")
def alterar_chave(nome: str, chave: Chave):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Verificando se a chave existe
        cur.execute("SELECT * FROM chaves WHERE nome = %s", (nome,))
        resultado = cur.fetchone()
        if resultado is None:
            return {"message": "Chave não encontrada!"}
        # Executando a consulta SQL para alterar a chave pelo nome
        cur.execute("UPDATE chaves SET nome = %s, situacao = %s, status = %s WHERE nome = %s", (chave.nome, chave.situacao, chave.status, nome))
        # Confirmando a transação
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Chave alterada com sucesso!"}
    except (Exception, psycopg2.Error) as error:
        raise HTTPException(status_code=400, detail=str(error))

# Definindo uma rota GET que busca pelos nomes para "/chaves"
@router.get("/chaves/{nome}")
def buscar_chave(nome: str):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Executando a consulta SQL para buscar a chave pelo nome
        cur.execute("SELECT * FROM chaves WHERE nome = %s", (nome,))
        resultado = cur.fetchone()
        if resultado is None:
            return {"message": "Chave não encontrada!"}
        cur.close()
        conn.close()
        return {"chave": resultado}
    except (Exception, psycopg2.Error) as error:
        raise HTTPException(status_code=400, detail=str(error))
