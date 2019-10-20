import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql
import datetime
import time

from projeto import *

class TestProjeto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global config
        cls.connection = pymysql.connect(
            host=config['HOST'],
            user=config['USER'],
            password=config['PASS'],
            database='MEGDA'
        )

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def setUp(self):
        conn = self.__class__.connection
        with conn.cursor() as cursor:
            cursor.execute('START TRANSACTION')

    def tearDown(self):
        conn = self.__class__.connection
        with conn.cursor() as cursor:
            cursor.execute('ROLLBACK')

    def commit(self):
        conn = self.__class__.connection
        with conn.cursor() as cursor:
            cursor.execute('COMMIT')

    def testa_adiciona_usuario(self):

        conn = self.__class__.connection
        self.setUp()

        adiciona_usuario(conn, "Bruno", "meuaaidl@eu.com", "SP")
        if len(select_usuarios(conn))<1:
            self.fail('Falhou ao adicionar uma pessoa.')

        adiciona_usuario(conn, "brundwaftrf9o", "meuefl@eu.com", "RJ")
        if len(select_usuarios(conn))<2:
            self.fail('Falhou ao adicionar duas pessoas.')
        adiciona_usuario(conn, "brundwaftawdrf9o", "meuawl@eu.com", "SP")
        adiciona_usuario(conn, "brundawdwaftrf9o", "medfmail@eu.com", "ES")
        adiciona_usuario(conn, "brunawdwaftrf9o", "maail@eu.com", "RJ")
        adiciona_usuario(conn, "brawdundwaftrf9o", "meuefaaail@eu.com", "SP")
        
        self.commit()

    def testa_adiciona_preferencia(self):
        conn = self.__class__.connection
        self.setUp()
        adiciona_preferencia(conn, "banana", 1)
        if len(select_pref(conn))<1:
            self.fail('Falhou ao adicionar uma preferencia.')

        adiciona_preferencia(conn, "maca", 1)
        if len(select_pref(conn))<2:
            self.fail('Falhou ao adicionar duas preferencias.')
        self.commit()

    def testa_adiciona_post(self):
        conn = self.__class__.connection

        self.setUp()
        adiciona_usuario(conn, "brunasawdawdd9o", "meueaaddwdmail@eu.com", "SSP-")

        adiciona_post(conn, 1, "titulo1", "url interessante1", "texto @banana #mosca @bananoide")
        if len(select_posts(conn))<1:
            self.fail('Falhou ao adicionar um post.')

        #adiciona_post(conn, 1, "titulo1", "url interessante", "texto @banana #mosca @bananoide")
        #if not len(select_posts(conn))<2:
        #    self.fail('Falhou ao adicionar um post repetido.')

        adiciona_post(conn, 1, "titul1o1", "url inte123essante 1", "Nao usar o mesmo texto @bana123na #voadora @bananoide33")
        if len(select_posts(conn))<2:
            self.fail('Falhou ao adicionar dois posts.')

        self.commit()
    
    def testa_deleta_post(self):
        conn = self.__class__.connection
        self.setUp()

        delete_post(conn, 1)
        delete_post(conn, 2)
        delete_post(conn, 3)
        delete_post(conn, 4)
        delete_post(conn, 5)
        if len(select_posts_ativos(conn))>1:
            self.fail('Falhou ao adicionar uma preferencia.')
        self.commit()




    def testa_log(self):
        conn = self.__class__.connection
        self.setUp()
        adiciona_log_info(conn, "1.1.1.1", "firefox", "motorola", 1)
        if len(select_logs(conn))<1:
            self.fail('Falhou ao adicionar uma pessoa.')

        adiciona_log_info(conn, "1.1.1.1", "chrome", "motorola", 1)
        if len(select_logs(conn))<2:
            self.fail('Falhou ao adicionar duas pessoas.')
        self.commit()








    def testa_tags_mencionadas(self):
        conn = self.__class__.connection
        self.setUp()


        adiciona_log_info(conn, "1.1.2.1", "firefox", "motorola", 1)


        adiciona_log_info(conn, "1.1.3.1", "chrome", "motorola", 2)
        adiciona_log_info(conn, "1.1.4.1", "chrome", "motorola", 3)

        adiciona_log_info(conn, "1.1.5.1", "firefox", "motorola", 4)

        adiciona_log_info(conn, "1.1.6.1", "chrome", "motorola", 5)
        adiciona_log_info(conn, "1.1.7.1", "safari", "motorola", 6)

        adiciona_log_info(conn, "1.1.8.1", "safari", "motorola", 7)


        if (len(acessos_por_aparelho_navergador(conn)) != 3) :
            self.fail('Falhou no agrupamento.')



        self.commit()

    def testa_log_agrupado(self):
        conn = self.__class__.connection
        self.setUp()


        adiciona_post(conn, 4, "PostTesteTags1", "url ainte123essante", "Nao usar o mesmeo texto @Bruno #voaadora @bananquede33")
        adiciona_post(conn, 2, "PostTesteTags2", "url adinte123essante", "Nao usar o mesmoa texto @Bruno #voaddora @banananoide33")
        adiciona_post(conn, 3, "PostTesteTags3", "url dinte123essante", "Nao usar o mesmgo texto @Bruno #voaadora @baodinoide33")
        adiciona_post(conn, 1, "PostTesteTags3", "url dinte123essante", "Nao usar o mesmgo texto @Bruno123 #voaadora @baodinoide33")

        if (len(referencias_por_usuario(conn, "Bruno")) != 3):
            self.fail('Falhou nas tags.')


        #self.commit() Nao dar commit

    def testa_deleta_post(self):
        conn = self.__class__.connection
        self.setUp()

        adciona_reacao(conn, 1, 1, 1)
        adciona_reacao(conn, 1, 1, 2)
        adciona_reacao(conn, 1, 1, 3)
        adciona_reacao(conn, 1, 1, 4)
        

        if (len(select_reacoes(conn)) != 4):
            self.fail('Falhou nas tags.')

        adciona_reacao(conn, 1, 1, 5)
        if (len(select_reacoes(conn)) == 4):
            self.fail('Falhou nas tags ao adicionar mais uma.')

        self.commit()

    def testa_ordem_inversa_insercao(self):
        conn = self.__class__.connection
        self.setUp()



        if (len(select_posts_ativos_ordem_cronologica(conn)) != 6):
            self.fail('Falhou ao receber os post ja commitados.')
        time.sleep(1)
        adiciona_post(conn, 1, "PostTesteTags3", "url dinte123essante", "Nao usar o mesmgo texto @Bruno123 #voaadora @baodinoide33")
        datas = [x[-1] for x in select_posts_ativos_ordem_cronologica(conn)]

        if ((datas[0]<datas[-1])):
            self.fail('Nao retorno na ordem inversa cronologica.')

        self.commit()


    def testa_usuario_famoso(self):
        conn = self.__class__.connection
        self.setUp()



        if (len(select_usuarios_famosos_por_cidade(conn, "SP")) != 2):
            self.fail('Falhou no usuario mais famoso de Sao Paulo.')
        if (len(select_usuarios_famosos_por_cidade(conn, "RJ")) != 1):
            self.fail('Falhou no usuario mais famoso do Rio.')

        self.commit()
    
    def testa_usuarios_dia(self):
        conn = self.__class__.connection
        self.setUp()



        if (len(acessos_no_dia(conn, 10))!=2):
            self.fail('Falhou ao tentar checar os logs do dia.')


    def testa_pegaroslinks_por_passaro(self):
        conn = self.__class__.connection
        self.setUp()



        if (len(url_por_passaros(conn, "voaadora")) != 3): #tres referenciando o prinmeiro post 
            self.fail('Falhou ao achar urls.')

        


    










      

def run_sql_script(filename):
    global config
    with open(filename, 'rb') as f:
        subprocess.run(
            [
                config['MYSQL'], 
                '-u', config['USER'], 
                '-p' + config['PASS'], 
                '-h', config['HOST']
            ], 
            stdin=f
        )

def setUpModule():
    filenames = [entry for entry in os.listdir() 
        if os.path.isfile(entry) and re.match(r'.*_\d{3}\.sql', entry)]
    for filename in filenames:
        run_sql_script(filename)

def tearDownModule():
    run_sql_script('tear_down.sql')

if __name__ == '__main__':
    global config




    
    with open('config_tests.json', 'r') as f:
        config = json.load(f)

    connn = pymysql.connect(
        host=config['HOST'],
        user=config['USER'],
        password=config['PASS'],
        database='MEGDA'
    )


    setUpModule()

    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)



