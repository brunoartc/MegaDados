from fastapi import FastAPI
from projeto import *
import json
from pydantic import BaseModel
from starlette.requests import Request

app = FastAPI()


with open('config_tests.json', 'r') as f:
    config = json.load(f)


conn = pymysql.connect(
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
    IdUsuario: int
    nomePassaro: str
    


class Reacao(BaseModel):
    Reacao: int
    PostId: int
    IdUsuario: int


class Post(BaseModel):
    IdUsuario: int
    Titulo: str
    Url: str = None
    Texto: str = None


@app.post("/user")
def adiciona_usuario_server(usuario: Usuario):
    return adiciona_usuario(conn, usuario.nome, usuario.email, usuario.cidade)


@app.post("/user/pref")
def adiciona_preferencia_server(preferencia: Preferencia):
    return adiciona_preferencia(conn, preferencia.nomePassaro,  preferencia.IdUsuario)


@app.post("/posts/reaction")
def adciona_reacao_server(reacao: Reacao):
    return {"obs" : "resposta pdoe vir incoerente por usar um id de post fixo", "data":adciona_reacao(conn, reacao.Reacao, reacao.PostId, reacao.IdUsuario)}

@app.put("/posts/reaction")
def adciona_reacao_server(reacao: Reacao):
    return {"obs" : "resposta pdoe vir incoerente por usar um id de post fixo", "data":edita_reacao(conn, reacao.Reacao, reacao.PostId, reacao.IdUsuario)}


@app.post("/posts")
def adiciona_post_server(post: Post):
    adiciona_post(conn, post.IdUsuario, post.Titulo, post.Url, post.Texto)


@app.get("/user/all")
def select_usuarios_server():
    return select_usuarios(conn)


@app.get("/logs")
def select_logs_server():
    return select_logs(conn)


@app.get("/user/prefs")
def select_pref_server():
    return select_pref(conn)


@app.get("/posts/reaction")
def select_reacoes_server():
    return select_reacoes(conn)


@app.get("/posts/all")
def select_posts_server(request: Request):
    ip = request.client.host
    info = request.headers["user-agent"].split()
    print(info)
    adiciona_log_info(conn, ip, info[-2], info[1], 1)
    return select_posts(conn)


@app.get("/posts/active")
def select_posts_ativos_server():
    return select_posts_ativos(conn)


@app.get("/posts/order/timestamp")
def select_posts_ativos_ordem_cronologica_server():
    return select_posts_ativos_ordem_cronologica(conn)


@app.get("/logs/devices")
def acessos_por_aparelho_navergador_server():
    return acessos_por_aparelho_navergador(conn)


@app.get("/user/popularity/{nome_cidade}")
def select_usuarios_famosos_por_cidade_server(nome_cidade):
    return select_usuarios_famosos_por_cidade(conn, nome_cidade)


@app.get("/user/references/{nome_usuario}")
def referencias_por_usuario_server(nome_usuario):
    print(nome_usuario)
    return {"obs" : "resposta pdoe vir incoerente por usar um id de post fixo", "data": referencias_por_usuario(conn, nome_usuario)}


@app.get("/logs/day/{Limite}")
def acessos_no_dia_server(Limite):
    return acessos_no_dia(conn, Limite)


@app.get("/images/{passaro}")
def url_por_passaros_server(passaro):
    return url_por_passaros(conn, passaro)


@app.delete("/{id}")
def delete_post_server(id):
    return delete_post(conn, id)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
