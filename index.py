'''
Projeto final de programação - Nicolas L. Kaminski

Professor: Yuri

print() - Saída limpa de código
'''
# Conexao com o Banco e Importação
import time as t  # Importando a biblioteca time
import sqlite3
from sqlite3 import Error

#=======================================================
import connection
import submit
import checkIn
import checkOut
import change
import reports
import leave


vcon = connection.con_BD()

#=======================================================
t.sleep(1)  # Descanso de 1 segundo
print('SEJA BEM-VINDO')
t.sleep(1)  # Descanso de 1 segundo

print()  # Saída limpa de código

# Home do Projeto
while True:

    t.sleep(1)  # Descanso de 1 segundo

    print("======== Menu ========")
    print('- Cadastrar uma reserva (Opção 1)')
    print('- Entrada do cliente [Check in] (Opção 2)')
    print('- Saída do cliente [Check out] (Opção 3)')
    print('- Alterar reserva (Opção 4)')
    print('- Relatórios (Opção 5)')
    print('- Saida, Volte Sempre! (Opção 6)')

    print()  # Saída limpa do código

    opc = int(input('O que deseja fazer ? '))

    print()  # Saída limpa do código

    if opc == 1:
        # Chama a função de cadastro do arquivo submit / Faz o cadastro no banco
        submit.f_Submit(vcon)

    elif opc == 2:
        # Chama a função de check-In do arquivo checkIn / Faz o Check-In na reserva
        checkIn.f_Check_In(vcon) 

    elif opc == 3:
        # Chama a função de check-Out do arquivo checkOut / Faz o Check-Out na reserva
        checkOut.f_Check_Out(vcon)

    elif opc == 4:
        # Chama a função de alteração do arquivo change / Faz a alteração da reserva
        change.f_Total_Alt(vcon)

    elif  opc == 5:
        # Chama a função de relatórios do arquivo reports / Gera o relatorio de arquivo
        reports.f_Report(vcon)

    elif  opc == 6:
        # Chama a função de saída do arquivo leave / Sai do sistema
        leave.f_Leave_Program(vcon)
    
    else:
        print('A opção digitada não existe, tente novamente!')
        opc = int(input('Digite uma opção válida: '))
        print() # Saída limpa do código
        t.sleep(1)  # Descanso de 1 segundo
        # Olá Git


