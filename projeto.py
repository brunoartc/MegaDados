import pymysql


global id_post
id_post = 1


def adiciona_usuario(conn, nome, email, cidade):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                'INSERT INTO Usuarios (Nome, Email, Cidade) VALUES (%s, %s, %s)', (nome, email, cidade))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso inserir Usuario na tabela Usuarios')


def adiciona_preferencia(conn, nomePassaro, IdUsuario):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                'INSERT INTO Preferencias (PassaroNome, IdUsuario) VALUES (%s, %s)', (nomePassaro, IdUsuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso inserir Usuario na tabela Usuarios')


def adciona_tag(conn, typee, PostId, Conteudo):

    with conn.cursor() as cursor:
        try:
            cursor.execute(
                'INSERT INTO Tags (Typee, PostId, Conteudo) VALUES (%s, %s, %s)', (typee, PostId, Conteudo))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso inserir Tags')




def adciona_reacao(conn, Reacao, PostId, IdUsuario):

    with conn.cursor() as cursor:
        try:
            cursor.execute(
                'INSERT INTO Joinhas (Reacao, PostId, IdUsuario) VALUES (%s, %s, %s)', (Reacao, PostId, IdUsuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso inserir reacao ao post')

def select_reacoes(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM Joinhas')
        res = cursor.fetchall()
        joia = tuple(x[0] for x in res)
        return joia

def select_posts(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM Post')
        res = cursor.fetchall()
        posts = tuple(x[0] for x in res)
        return posts


def select_posts_ativos(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM Post WHERE Existe=1')
        res = cursor.fetchall()
        posts = tuple(x[0] for x in res)
        return posts


def select_posts_ativos_ordem_cronologica(conn): #TODO: need unit test
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM Post WHERE Existe=1 ORDER BY timestampe DESC')
        res = cursor.fetchall()
        posts = [x for x in res]
        return posts


def select_usuarios_famosos_por_cidade(conn, nome_cidade): #TODO: need unit test
    with conn.cursor() as cursor:
        cursor.execute('SELECT COUNT(*) AS POSTS,IdUsuario FROM Post INNER JOIN usuarios ON Post.IdUsuario = usuarios.id WHERE Cidade=%s GROUP BY IdUsuario', nome_cidade)
        res = cursor.fetchall()
        usuarios = tuple(x[0] for x in res)
        return usuarios

def referencias_por_usuario(conn, nome_usuario):
    with conn.cursor() as cursor:
        cursor.execute('SELECT Conteudo AS Referenciado, IdUsuario AS Referencia_Id_Usuario, PostId AS NoPost FROM Tags INNER JOIN Post ON Tags.PostId = Post.Id WHERE Conteudo = %s', nome_usuario)
        res = cursor.fetchall()
        usuarios = [str(x) for x in res]
        return usuarios
        


def acessos_por_aparelho_navergador(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT Aparelho,Navegador,COUNT(*) AS TOTAL FROM log GROUP BY Aparelho,Navegador')
        res = cursor.fetchall()
        conta = tuple(x[0] for x in res)
        return conta










def select_usuarios(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM Usuarios')
        res = cursor.fetchall()
        usuarios = tuple(x[0] for x in res)
        return usuarios


def select_logs(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM Log')
        res = cursor.fetchall()
        logg = tuple(x[0] for x in res)
        return logg


def select_pref(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM Preferencias')
        res = cursor.fetchall()
        prefs = tuple(x[0] for x in res)
        return prefs


def achar_palavras_chave(Texto):
    tagsAt = []
    tagsHash = []
    i = 0
    while Texto.find("@", i) != -1 or i == len(Texto):
        i = Texto.find("@", i) + 1
        tagsAt.append(Texto[i:Texto.find(" ", i)])
        i += 1
    i = 0
    while Texto.find("#", i) != -1 or i == len(Texto):
        i = Texto.find("#", i) + 1
        tagsHash.append(Texto[i:Texto.find(" ", i)])
        i += 1

    return [tagsAt, tagsHash]






def adiciona_post(conn, IdUsuario, Titulo, Url, Texto):
    tagsAt = []
    tagsHash = []
    i = 0
    [tagsAt, tagsHash] =  achar_palavras_chave(Texto)
    global id_post
    id_post +=1

    
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                'INSERT INTO Post (IdUsuario, Titulo, Url, Texto) VALUES (%s, %s, %s, %s)', (IdUsuario, Titulo, Url, Texto))
            cursor.execute(
                'COMMIT')
            for i in tagsAt:

                adciona_tag(conn,2, 1, i)

            for i in tagsHash:
                adciona_tag(conn,2, 1, i)
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso inserir Usuario na tabela Posts')


def delete_post(conn, id):
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE Post SET Existe=0 where Id=%s', (id))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao deleter o post')


def adiciona_log_info(conn, ip, navegador, aparelho, idusuario):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO Log (Ip, Aparelho, Navegador, IdUsuario) VALUES (%s, %s, %s, %s)',
                           (ip, aparelho, navegador, idusuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao loggar algo')



    


def commit(conn):
    with conn.cursor() as cursor:
        try:
            cursor.execute('COMMIT')
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao commitar')

def adciona_usuario_e_post(conn, IdUsuario, Titulo, Url, Texto, nome, email, cidade):
    adiciona_post(conn, IdUsuario, Titulo, Url, Texto)

