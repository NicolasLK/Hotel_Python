# Conexao com o Banco e Importação
import time as t  # Importando a biblioteca time
import sqlite3
from sqlite3 import Error
import connection

vcon = connection.con_BD()
#=======================================================
#======================== Funções ======================

def f_Submit_sql(con, sql):
    try:
        c=con.cursor()
        c.execute(sql)
        con.commit()
        print("Reserva cadastrada!")
    except Error as ex:
        print(ex) 

#=======================================================
def f_Submit(vcon):
    while True:
        print("===== Cadastro de reservas =====")
        t.sleep(0.5)  # Descanso de 0.5 segundo
        nome_T = input("Informe o Nome do Titular: ")
        cpf = input("Informe o Cpf do Titular: ")

        if len(cpf) < 11:
            print("Cpf Invalido!")
            cpf = input("Informe o Cpf novamente: ")

        else:
         ...

        nP = int(input("Informe a quantidade de pessoas: "))
        if nP <= 0: 
            print("Quantidade de pessoas invalida!")
            nP = int(input("Informe a quantidade novamente: "))

        else:   
            ...

        nD = int(input("Informe a Diaria: "))
        if nD <= 0: 
            print("Diaria invalida!")
            nD = int(input("Informe a diaria novamente: "))

        else:   
            ...

        typeQ = ''

        while True:
            print('Tipos de Quartos: ')
            print('S - Standart R$100.00 (Opção 1)')
            print('D - Deluxe R$200.00 (Opção 2)')
            print('P - Premium R$300.00 (Opção 3)')

            opc_Q = int(input('Digite o tipo de Quarto:'))

            if opc_Q == 1:
                typeQ = "S"
                break

            elif opc_Q == 2:
                typeQ = "D"
                break

            elif opc_Q == 3:
                typeQ = "P"
                break
    
            else:
                print('Opcao de Quarto Invalida !')

        if opc_Q == 1:
            valorT = 100 * nP * nD

        elif opc_Q == 2:
            valorT = 200 * nP * nD   

        else:
            valorT = 300 * nP * nD   


        sts = 'R'

        if (nome_T == '') or (cpf == '') or (nP == 0) or (nD == 0) or (valorT == 0):
            print('Reservas não cadastradas!')

        else:
            ...
            break
            

    # Comando INSERT (Querry)
    vsql = "INSERT INTO tb_reservas (Nome_Titular,Cpf,Num_Pessoas,Diaria,Tipo_Quarto,Status,Valor_Total) VALUES ('"+nome_T+"','"+cpf+"',"+str(nP)+","+str(nD)+",'"+typeQ+"','"+sts+"',"+str(valorT)+")"


    # Chamando a função para inserir a reserva
    f_Submit_sql(vcon, vsql)
