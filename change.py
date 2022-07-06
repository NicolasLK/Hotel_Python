# Conexao com o Banco e Importação
import time as t  # Importando a biblioteca time
import sqlite3
from sqlite3 import Error
import connection

vcon = connection.con_BD()
#=======================================================
#======================== Funções ======================

# Função para dar SELECT
def f_Search_sql(con, sql):
    c=con.cursor()
    c.execute(sql)
    records=c.fetchall()
    return records

# Função para dar UPDATE
def f_Alt(con, sql):
    try:
        c=con.cursor()
        c.execute(sql)
        con.commit()
    except Error as ex:
        print(ex) 
    finally:
        print("Alteração realizada com sucesso!")

#=======================================================
def f_Total_Alt(vcon):

    print("===== Alteração =====")
    t.sleep(0.5)  # Descanso de 0.5 segundo

    print()

    t.sleep(0.5)  # Descanso de 0.5 segundo

    print("============ Menu ============")
    print("==============================")
    print("- Alteração do Nº de pessoas (Opção 1)")
    print('- Alteração do tipo de quarto (Opção 2)')
    print('- Alteração da diaria (Opção 3)')
    print('- Alteração do status (Opção 4)')
    print('- Saida (Opção 5)')
    print("==============================")

    print()

    opc = int(input("O que deseja fazer ?"))

    t.sleep(0.5)  # Descanso de 0.5 segundo
    while True:

        if opc == 1: # Alteração Nº de pessoas

            print("===== Alteração de pessoas =====")
            t.sleep(0.5)  # Descanso de 0.5 segundo

            cpf = input("Informe o Cpf que deseja pesquisar: ")

            if cpf == "":
                print("Cpf invalido!")
                cpf = input("Informe o Cpf novamente: ")
    
            else:
                ...

            vsqlS = "SELECT * FROM tb_reservas WHERE Cpf = '"+cpf+"'" # Comando SELECT (Querry)
            recordsT = f_Search_sql(vcon, vsqlS) # Chama a função para dar SELECT

            formatted_users = []

            for t_users in recordsT:
                formatted_users.append(list(t_users))

            print(formatted_users)

            qtd_regs = len(formatted_users)

            if qtd_regs >= 2: # Condição de 2 ou + registros

                id_reg = int(input("Escolha o registro para alteração: ")) # Indice no array
                reg_select = formatted_users[id_reg]

                nP = int(input("Informe a quantidade de pessoas: "))

                if nP <= 0:
                    print("Nº de pessoas invalido!")
                    nP = int(input("Inform o Nº de pessoas novamente: "))

                else:
                    ...
            
                if reg_select[5] == "S":
                    typeQ = 100
                elif reg_select[5] == "D":
                    typeQ = 200
                else:
                    typeQ = 300

                valorT = nP * reg_select[4] * typeQ

                id_user = int(input("Informe o Id da reserva: ")) # Indice no banco
            
                # Comando UPDATE (Querry)
                vsqlP_2 = "UPDATE tb_reservas SET Num_Pessoas= "+str(nP)+", Valor_Total= "+str(valorT)+" WHERE Cpf = '"+cpf+"' AND Id = "+str(id_user)+""
                f_Alt(vcon, vsqlP_2) # Chama a função de Alteração

            else: # Condição 1 registro

                nP = int(input("Informe a quantidade de pessoas: "))

                if nP <= 0:
                    print("Nº de pessoas invalido!")
                    nP = int(input("Inform o Nº de pessoas novamente: "))

                else:
                    ...

                if formatted_users[0][5] == "S":
                    typeQ = 100

                elif formatted_users[0][5] == "D":
                    typeQ = 200

                else: 
                    typeQ = 300

                diaria = formatted_users[0][4]

                valorT = nP * diaria * typeQ

                # Comando UPDATE (Querry)
                vsqlP_1 = "UPDATE tb_reservas SET Num_Pessoas= "+str(nP)+", Valor_Total= "+str(valorT)+" WHERE Cpf ='"+cpf+"'"
                f_Alt(vcon, vsqlP_1)# Chama a função de Alteração

            break

        elif opc == 2: # Alteração de tipo de quarto
            print("===== Alteração de quarto =====")
            t.sleep(0.5)  # Descanso de 0.5 segundo

            cpf = input("Informe o Cpf que deseja pesquisar: ")

            if cpf == "":
                print("Cpf invalido!")
                cpf = input("Informe o Cpf novamente: ")
    
            else:
                ...

            vsqlS = "SELECT * FROM tb_reservas WHERE Cpf = '"+cpf+"'" # Comando SELECT (Querry)
            recordsT = f_Search_sql(vcon, vsqlS) # Chama a função para dar SELECT

            formatted_users = []

            for t_users in recordsT:
                formatted_users.append(list(t_users))

            print(formatted_users)

            qtd_regs = len(formatted_users)

            if qtd_regs >= 2: # Condição de 2 ou + registros

                id_reg = int(input("Escolha o registro para alteração: ")) # Indice no array
                reg_select = formatted_users[id_reg]

                typeQ = ""

                while True: # Escolha do tipo de quarto

                    t.sleep(0.5)  # Descanso de 0.5 segundo
                    print("===== Tipos de Quartos: =====")
                    print("S - Standart R$100.00 (Opção 1)")
                    print("D - Deluxe R$200.00 (Opção 2)")
                    print("P - Premium R$300.00 (Opção 3)")
                    print("==============================")

                    t.sleep(0.2)  # Descanso de 0.2 segundo

                    opc_Q = int(input("Informe a opção de quarto: "))

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
                        print("Opção de quarto invalida!")
                
                if opc_Q == 1:
                    valorT = 100 * reg_select[3] * reg_select[4]
            
                elif opc_Q == 2:
                    valorT = 200 * reg_select[3] * reg_select[4]
            
                else:
                    valorT = 300 * reg_select[3] * reg_select[4]

                id_user = int(input("Informe o Id da reserva: ")) # Indice no banco
            
                # Comando UPDATE (Querry)
                vsqlQ_2 = "UPDATE tb_reservas SET Tipo_Quarto= '"+typeQ+"', Valor_Total= "+str(valorT)+" WHERE Cpf = '"+cpf+"' AND Id = "+str(id_user)+""
                f_Alt(vcon, vsqlQ_2) # Chama a função de Alteração

            else: # Condição 1 registro

                typeQ = ""

                while True: # Esolha do tipo de quarto

                    t.sleep(0.5)  # Descanso de 0.5 segundo
                    print("===== Tipos de Quartos: =====")
                    print("S - Standart R$100.00 (Opção 1)")
                    print("D - Deluxe R$200.00 (Opção 2)")
                    print("P - Premium R$300.00 (Opção 3)")
                    print("==============================")

                    t.sleep(0.2)  # Descanso de 0.2 segundo

                    opc_Q = int(input("Informe a opção de quarto: "))

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
                        print("Opção de quarto invalida!")
                
                    if opc_Q == 1:
                        valorT = 100 * formatted_users[0][3] * formatted_users[0][4]

                    elif opc_Q == 2:
                        valorT = 200 * formatted_users[0][3] * formatted_users[0][4]

                    else:
                        valorT = 300 * formatted_users[0][3] * formatted_users[0][4]
                        
                # Comando UPDATE (Querry)
                vsqlQ_1 = "UPDATE tb_reservas SET Tipo_Quarto= '"+typeQ+"', Valor_Total= "+str(valorT)+" WHERE Cpf ='"+cpf+"'"
                f_Alt(vcon, vsqlQ_1) # Chama a função de Alteração

            break
                
        elif opc == 3: # Alteração de diaria

            print("===== Alteração de diária =====")
            t.sleep(0.5)  # Descanso de 0.5 segundo

            cpf = input("Informe o Cpf que deseja pesquisar: ")

            if cpf == "":
                print("Cpf invalido!")
                cpf = input("Informe o Cpf novamente: ")
    
            else:
                ...

            vsqlS = "SELECT * FROM tb_reservas WHERE Cpf = '"+cpf+"'" # Comando SELECT (Querry)
            recordsT = f_Search_sql(vcon, vsqlS) # Chama a função para dar SELECT

            formatted_users = []

            for t_users in recordsT:
                formatted_users.append(list(t_users))

            print(formatted_users)

            qtd_regs = len(formatted_users)

            if qtd_regs >= 2: # Condição de 2 ou + registros

                id_reg = int(input("Escolha o registro para alteração: ")) # Indice no array
                reg_select = formatted_users[id_reg]

                diaria = int(input("Informe a diária: "))

                if diaria <= 0:
                    print("Diária invalida!")
                    diaria = int(input("Informe a diária novamente: "))

                else:
                    ...
            
                if reg_select[5] == "S":
                    typeQ = 100
                elif reg_select[5] == "D":
                    typeQ = 200
                else:
                    typeQ = 300

                valorT = reg_select[3] * diaria * typeQ

                id_user = int(input("Informe o Id da reserva: ")) # Indice no banco
            
                # Comando UPDATE (Querry)
                vsqlD_2 = "UPDATE tb_reservas SET Diaria= "+str(diaria)+", Valor_Total= "+str(valorT)+" WHERE Cpf = '"+cpf+"' AND Id = "+str(id_user)+""
                f_Alt(vcon, vsqlD_2) # Chama a função de alteração

            else: # Condição 1 registro
                diaria = int(input("Informe a diária: "))

                if diaria <= 0:
                    print("Diária invalida!")
                    diaria = int(input("Informe a diária novamente: "))

                else:
                    ...

                if formatted_users[0][5] == "S":
                    typeQ = 100

                elif formatted_users[0][5] == "D":
                    typeQ = 200

                else: 
                    typeQ = 300

                nP = formatted_users[0][3]

                valorT = nP * diaria * typeQ
            
                # Comando UPDATE (Querry)
                vsqlD_1 = "UPDATE tb_reservas SET Num_Pessoas= "+str(diaria)+", Valor_Total= "+str(valorT)+" WHERE Cpf ='"+cpf+"'"
                f_Alt(vcon, vsqlD_1)# Chama a função de Alteração

            break

        elif opc == 4: # Alteração de status
            print("===== Alteração de status =====")
            t.sleep(0.5)  # Descanso de 0.5 segundo

            cpf = input("Informe o Cpf que deseja pesquisar: ")

            if cpf == "":
                print("Cpf invalido!")
                cpf = input("Informe o Cpf novamente: ")
    
            else:
                ...

            # Comando SELECT (Querry)
            vsqlS = "SELECT * FROM tb_reservas WHERE Cpf = '"+cpf+"'" 
            recordsT = f_Search_sql(vcon, vsqlS) # Chama a função para dar SELECT

            formatted_users = []

            for t_users in recordsT:
                formatted_users.append(list(t_users))

            print(formatted_users)

            qtd_regs = len(formatted_users)

            if qtd_regs >= 2: # Condição de 2 ou + registros

                sts = "C"

                id_user = int(input("Informe o Id da reserva: ")) # Indice no banco

                # Comando UPDATE (Querry)
                vsqlS_2 = "UPDATE tb_reservas SET Status= '"+sts+"' WHERE Cpf = '"+cpf+"' AND Id = "+str(id_user)+""
                f_Alt(vcon, vsqlS_2) # Chama a função de alteração

            else: # Condição de 1 registro

                sts = "C"

                # Comando UPDATE (Querry)
                vsqlS_1 = "UPDATE tb_reservas SET Status= '"+sts+"' WHERE Cpf = '"+cpf+"'"
                f_Alt(vcon, vsqlS_1) # Chama a função de alteração

            break

        elif opc == 5: # Saida da alteração
            break

        else: # Caso opção digitada não exista
            print('A opção digitada não existe, tente novamente!')
            opc = int(input('Digite uma opção válida: '))
            print() # Saída limpa do código

