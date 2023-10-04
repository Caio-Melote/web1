from fastapi import APIRouter
from fastapi.responses import JSONResponse
from database.connection import get_db_connection

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