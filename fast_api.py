from fastapi import FastAPI
from projeto import *

app = FastAPI()


connn = pymysql.connect(
        host=config['HOST'],
        user=config['USER'],
        password=config['PASS'],
        database='MEGDA'
)


class Usuario(BaseModel):
    nome: str
    email: str
    cidade: str

class Preferencia(BaseModel):
    nomePassaro: str
    idUsuario: int

class Reacao(BaseModel):
    Reacao: str
    PostId: int
    IdUsuario: int
@app.post("/")
def adiciona_usuario( usuario : Usuario)

@app.post("/")
def adiciona_preferencia( preferencia : Preferencia)

@app.post("/")
def adciona_reacao( reacao : Reacao)

def select_usuarios(conn)


def select_logs(conn)


def select_pref(conn)


@app.get("/")
def select_reacoes_server(conn)

@app.get("/")
def select_posts_server(conn)

@app.get("/")
def select_posts_ativos_server(conn)

@app.get("/")
def select_posts_ativos_ordem_cronologica_server(conn)

@app.get("/")
def acessos_por_aparelho_navergador_server(conn)

@app.get("/{nome_cidade}")
def select_usuarios_famosos_por_cidade_server( nome_cidade)


@app.get("/{nome_usuario}")
def referencias_por_usuario_server( nome_usuario)


@app.get("/{Limite}")
def acessos_no_dia_server( Limite)

@app.get("/{passaro}")
def url_por_passaros_server( passaro)


        
def adiciona_post( IdUsuario, Titulo, Url, Texto)


def delete_post( id)


def adiciona_log_info( ip, navegador, aparelho, idusuario)



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}