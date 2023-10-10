from fastapi import APIRouter
from fastapi.responses import JSONResponse
from database.connection import get_db_connection
from models.model_chave import Chave

router = APIRouter()

@router.get("/chaves")
def listar_chaves():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM chaves")
        chaves = cur.fetchall()
        cur.close()
        conn.close()
        return JSONResponse(content={"chaves": chaves})
    except (Exception, psycopg2.Error) as error:
        return JSONResponse(content={"error": str(error)})
    
@router.get("/chaves_disp")
def listar_chaves_disponiveis():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM chaves WHERE status = 'disponivel'")
        chaves = cur.fetchall()
        cur.close()
        conn.close()
        return JSONResponse(content={"chaves": chaves})
    except (Exception, psycopg2.Error) as error:
        return JSONResponse(content={"error": str(error)})

@router.post("/chaves")
def adicionar_chave(chave: Chave):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO chaves (nome, situacao, status) VALUES (%s, %s, %s)", (chave.nome, chave.situacao, chave.status))
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Chave adicionada com sucesso!"}
    except (Exception, psycopg2.Error) as error:
        raise HTTPException(status_code=400, detail=str(error))
