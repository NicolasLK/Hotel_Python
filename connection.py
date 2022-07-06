import sqlite3
from sqlite3 import Error


def con_BD():
    path = sqlite3.connect("banco\\reservas.db") # Linha para conectar no BANCO
    con = None

    try:
        con = path

    except Error as ex:
        print(ex)
    return con

