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

#=======================================================
def f_Report(vcon):

    print("===== Geração de Relatório =====")
    t.sleep(0.5)  # Descanso de 0.5 segundo

    print()

    t.sleep(0.5)  # Descanso de 0.5 segundo

    print("============ Menu ============")
    print("==============================")
    print("- Relatório das reservas com status R (Opção 1)")
    print('- Relatório das reservas com status C (Opção 2)')
    print('- Relatório das reservas com status A (Opção 3)')
    print('- Relatório das reservas com status F (Opção 4)')
    print('- Relatório total recebido (Opção 5)')
    print('- Relatório de Reserva por pessoa (Opção 6)')
    print('- Saida (Opção 7)')
    print("==============================")

    print()

    opc = int(input("O que deseja fazer ?"))
    t.sleep(0.5)  # Descanso de 0.5 segundo

    count = 0

    while count == 0:

        if opc == 1: # Relatório status R
        
            vsqlR = "SELECT * FROM tb_reservas WHERE Status = 'R' "  # Comando SELECT (Querry)
            recordsT = f_Search_sql(vcon, vsqlR) # Chama a função para dar SELECT

            formatted_users = []

            for t_users in recordsT:
                formatted_users.append(list(t_users))

            print(formatted_users)

            qtd_regs = len(formatted_users)

            print("A quantidade de reservas com o Status 'R' é: " + str(qtd_regs))


        elif opc == 2: # Relatório status C
            vsqlC = "SELECT * FROM tb_reservas WHERE Status = 'C' "  # Comando SELECT (Querry)
            recordsT = f_Search_sql(vcon, vsqlC) # Chama a função para dar SELECT

            formatted_users = []

            for t_users in recordsT:
                formatted_users.append(list(t_users))

            print(formatted_users)

            qtd_regs = len(formatted_users)

            print("A quantidade de reservas com o Status 'C' é: " + str(qtd_regs))

        elif opc == 3: # Relatório status A

            vsqlA = "SELECT * FROM tb_reservas WHERE Status = 'A' "  # Comando SELECT (Querry)
            recordsT = f_Search_sql(vcon, vsqlA) # Chama a função para dar SELECT

            formatted_users = []

            for t_users in recordsT:
                formatted_users.append(list(t_users))

            print(formatted_users)

            qtd_regs = len(formatted_users)

            print("A quantidade de reservas com o Status 'A' é: " + str(qtd_regs))

        elif opc == 4: # Relatório status F

            vsqlF = "SELECT * FROM tb_reservas WHERE Status = 'F' "  # Comando SELECT (Querry)
            recordsT = f_Search_sql(vcon, vsqlF) # Chama a função para dar SELECT

            formatted_users = []

            for t_users in recordsT:
                formatted_users.append(list(t_users))

            print(formatted_users)

            qtd_regs = len(formatted_users)

            print("A quantidade de reservas com o Status 'F' é: " + str(qtd_regs))

        elif opc == 5: # Total recebido
            vsqlT = "SELECT SUM(Valor_Total) FROM tb_reservas WHERE Status = 'F' "  # Comando SELECT (Querry)
            recordsT = f_Search_sql(vcon, vsqlT) # Chama a função para dar SELECT

            formatted_users = []

            for t_users in recordsT:
                formatted_users.append(list(t_users))

            print("O total recebido é: " + str(formatted_users[0]))

        elif opc == 6: # Relatório por pessoa

            cpf = input("Informe o Cpf para pesquisar: ")

            vsqlP = "SELECT Nome_Titular FROM tb_reservas WHERE Cpf = '"+cpf+"' "  # Comando SELECT (Querry)
            recordsT = f_Search_sql(vcon, vsqlP) # Chama a função para dar SELECT

            formatted_users = []

            for t_users in recordsT:
                formatted_users.append(list(t_users))

            qtd_regs = len(formatted_users)

            print(formatted_users)

            print("Hospede: " + str(formatted_users[0]))
            print("Total de reservas: " + str(qtd_regs))
    
        elif opc == 7: # Saida forçada
            break

        else: # Caso opção digitada não exista
            print('A opção digitada não existe, tente novamente!')
            opc = int(input('Digite uma opção válida: '))
            print() # Saída limpa do código
    
        count = count + 1

