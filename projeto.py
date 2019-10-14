import pymysql









def adiciona_usuario(conn, nome, email, cidade):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO Usuarios (Nome, Email, Cidade) VALUES (%s, %s, %s)', (nome, email, cidade))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso inserir Usuario na tabela Usuarios')


def adiciona_preferencia(conn, nomePassaro, IdUsuario):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO Preferencias (PassaroNome, IdUsuario) VALUES (%s, %s)', (nomePassaro, IdUsuario))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso inserir Usuario na tabela Usuarios')

        
def adciona_tag(conn, PostId, Conteudo):
    
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO Tags (Typee, PostId, Conteudo) VALUES (%s, %s, %s)', (IdUsuario, PostId, Conteudo ))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso inserir Usuario na tabela Usuarios')



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

def adiciona_post(conn, IdUsuario, Titulo, Url, Texto):
    tagsAt = []
    tagsHash = []
    i =  0
    # while Texto.find("@", i)!=-1 or i == len(Texto):
    #     i = Texto.find("@") + 1
    #     print(i)
    #     tagsAt.append(Texto[i:Texto.find(" ")])
    #     i+=1
    # i = 0
    # while Texto.find("#", i)!=-1 or i == len(Texto) :
    #     i = Texto.find("#") +1
    #     tagsHash.append(Texto[i:Texto.find(" ")])
    #     i+=1

    id_post = len(select_posts(conn))

    for i in tagsAt:
        adciona_tag(conn, id_post, i)


    for i in tagsHash:
        adciona_tag(conn, id_post, i)


    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO Post (IdUsuario, Titulo, Url, Texto) VALUES (%s, %s, %s, %s)', (IdUsuario, Titulo, Url, Texto ))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Não posso inserir Usuario na tabela Usuarios')



def delete_post(conn, id):
    with conn.cursor() as cursor:
        try:
            cursor.execute('UPDATE Post SET Existe=0 where Id=%s', (id))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao deleter o post')




def adiciona_log_info(conn, ip, navegador, aparelho, idusuario):
    with conn.cursor() as cursor:
        try:
            cursor.execute('INSERT INTO Log (Ip, Aparelho, Navegador, IdUsuario) VALUES (%s, %s, %s, %s)', (ip, aparelho, navegador, idusuario ))
        except pymysql.err.IntegrityError as e:
            raise ValueError(f'Erro ao loggar algo')
