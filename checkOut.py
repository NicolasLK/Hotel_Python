# Conexao com o Banco e Importação
import time as t  # Importando a biblioteca time
import sqlite3
from sqlite3 import Error
import connection

vcon = connection.con_BD()
#=======================================================
#======================== Funções ======================

def f_Search_sql(con, sql):
    c=con.cursor()
    c.execute(sql)
    records=c.fetchall()
    return records

def f_checkOut_sql(con, sql):
    try:
        c=con.cursor()
        c.execute(sql)
        con.commit()
    except Error as ex:
        print(ex) 
    finally:
        print("Status Atualizado com sucesso!")

#=======================================================
def f_Check_Out(vcon):
    print("===== Check-Out =====")
    t.sleep(0.5)  # Descanso de 0.5 segundo

    cpf = input("Informe o Cpf que deseja pesquisar: ")

    if cpf == "":
        print("Cpf invalido!")
        cpf = input("Informe o Cpf novamente: ")
    
    else:
        ...

    vsqlS = "SELECT * FROM tb_reservas WHERE Cpf = '"+cpf+"'" # Comando SELECT (Querry)
    recordsT = f_Search_sql(vcon, vsqlS) # Resultado do SELECT

    formatted_users = []

    for t_users in recordsT:
        formatted_users.append(list(t_users))

    print(formatted_users)

    qtd_regs = len(formatted_users)


    if qtd_regs >= 2:

        id_user = int(input("Esolha o registro: ")) # Id no banco

        vsqlU_2 = "UPDATE tb_reservas SET Status='F' WHERE Cpf = '"+cpf+"' AND Id = "+str(id_user)+"" # Comando UPDATE (Querry)
        f_checkOut_sql(vcon, vsqlU_2) # Chamando a função de Check-Out

    else:

        vsqlU_1 = "UPDATE tb_reservas SET Status='F' WHERE Cpf = '"+cpf+"'" # Comando UPDATE (Querry)
        f_checkOut_sql(vcon, vsqlU_1) # Chamando a função de Check-Out

