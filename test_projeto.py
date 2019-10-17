import io
import json
import logging
import os
import os.path
import re
import subprocess
import unittest
import pymysql

from projeto import *

class TestProjeto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global config
        cls.connection = pymysql.connect(
            host=config['HOST'],
            user=config['USER'],
            password=config['PASS'],
            database='md'
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























    def testa_deleta_post(self):
        conn = self.__class__.connection
        adiciona_usuario(conn, "brunasawdawdd9o", "meueaaddwdmail@eu.com", "SSP-")
        adiciona_usuario(conn, "brunasaawdawwdawdd9o", "meueaadawddwdmail@eu.com", "SSaP-")
        adiciona_post(conn, 1, "titulo1", "url interessante", "texto @banana #mosca @bananoide")

        delete_post(conn, 1)
        delete_post(conn, 2)
        delete_post(conn, 3)
        delete_post(conn, 4)
        delete_post(conn, 5)
        print(len(select_posts_ativos(conn)))
        if len(select_posts_ativos(conn))>1:
            self.fail('Falhou ao adicionar uma preferencia.')

    def testa_adiciona_post(self):
        conn = self.__class__.connection


        adiciona_usuario(conn, "brunasawdawdd9o", "meueaaddwdmail@eu.com", "SSP-")

        adiciona_post(conn, 1, "titulo1", "url interessante", "texto @banana #mosca @bananoide")
        if len(select_posts(conn))<1:
            self.fail('Falhou ao adicionar uma preferencia.')

        adiciona_post(conn, 1, "titul1o1", "url inte123essante", "texto @bana123na #mosca @bananoide")
        if len(select_posts(conn))<2:
            self.fail('Falhou ao adicionar duas preferencias.')


    def testa_adiciona_preferencia(self):
        conn = self.__class__.connection


        adiciona_usuario(conn, "brunasd9o", "meueadwdmail@eu.com", "SSP-")
        adiciona_usuario(conn, "brunawdawdasd9o", "meueaawdawddwdmail@eawdau.coawdm", "SSPa-")
        adiciona_preferencia(conn, "banana", 1)
        if len(select_pref(conn))<1:
            self.fail('Falhou ao adicionar uma preferencia.')

        adiciona_preferencia(conn, "maca", 1)
        if len(select_pref(conn))<2:
            self.fail('Falhou ao adicionar duas preferencias.')

    
    def testa_adiciona_usuario(self):
        conn = self.__class__.connection

        adiciona_usuario(conn, "brunad9o", "meuawdemail@eu.com", "SaSP-")
        if len(select_usuarios(conn))<1:
            self.fail('Falhou ao adicionar uma pessoa.')

        adiciona_usuario(conn, "brundwaftrf9o", "meuefawdfmail@eu.com", "SSP-")
        if len(select_usuarios(conn))<2:
            self.fail('Falhou ao adicionar duas pessoas.')



    def testa_log(self):
        conn = self.__class__.connection

        adiciona_usuario(conn, "brun9o", "meuemail@eu.com", "SSP-")
        adiciona_usuario(conn, "brun9o", "meuema123123il@eu.com", "SSP-")
        print(len(select_usuarios(conn)))
        adiciona_log_info(conn, "1.1.1.1", "firefox", "motorola", 1)
        if len(select_logs(conn))<1:
            self.fail('Falhou ao adicionar uma pessoa.')

        adiciona_log_info(conn, "1.1.1.1", "chrome", "motorola", 1)
        if len(select_logs(conn))<2:
            self.fail('Falhou ao adicionar duas pessoas.')


  

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
        database='md'
    )

    # adiciona_usuario(connn, "brunasawawdawawddawdd9o", "meueaaddwdmail@eu.com", "SSP-") script so esta funcionando se adiciona 2 usuarios fora
    # adiciona_usuario(connn, "brunasaawdawwdaawdwdd9o", "meueaadawddwdmail@eu.com", "SSaP-")

    setUpModule()

    logging.basicConfig(filename=config['LOGFILE'], level=logging.DEBUG)
    unittest.main(verbosity=2)
