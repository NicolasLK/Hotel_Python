# Conexao com o Banco e Importação
import time as t  # Importando a biblioteca time
import sqlite3
from sqlite3 import Error
import connection

vcon = connection.con_BD()

#=======================================================
def f_Leave_Program(vcon):
    print('Saindo...')
    t.sleep(1.7)  # Descanso de 1.7 segundo
    exit()
