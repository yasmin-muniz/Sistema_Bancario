# Atribuindo data da transação e limite de transacao diaria

menu = """


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """
 
from datetime import datetime
lista_extrato = []

saldo = 1000
limite = 500
extrato = ""

numero_saques = 0
numero_transacoes = 0
valor_saque = 0
valor_deposito = 0

LIMITE_SAQUES = 3
LIMITE_TRANS_DIARIA = 10


while True:
    

    opcao = input (menu)
    data_atual = datetime.now()
    data_formatada = data_atual.strftime("%d-%m-%Y %H:%M:%S")

    if opcao in ("d","s"):
        if numero_transacoes == LIMITE_TRANS_DIARIA:
            print("Você atingiu o limite de transações diárias!") 
        else: 
            if opcao == "d": 
                valor_deposito =  float(input ('Qual valor a ser depositado?')) 
                saldo += valor_deposito 
                lista_extrato.append(f'Depósito: R$ {valor_deposito}, Data da transação: {data_formatada}')
                numero_transacoes += 1
            
            elif opcao == "s":
                valor_saque = float(input ('Qual valor a ser sacado?')) 
                if valor_saque > limite:
                    print ("O limite para saque é de R$500,00 reais") 
                elif valor_saque > saldo:
                    print("Não há saldo suficiente na conta!")
                elif numero_saques >= LIMITE_SAQUES:
                    print("Você atingiu o limite de saques diários!") 
                else:
                    saldo -= valor_saque
                    lista_extrato.append(f'Saque: R$ {valor_saque}, Data da transação: {data_formatada}')  
                    numero_saques += 1
                    numero_transacoes +=1
                    print(f"Saque de R${valor_saque} realizado com sucesso!")

    elif opcao == "e": 
        for transacao in lista_extrato:
            print(transacao)
        print(f"Saldo: R${saldo}")
            
    elif opcao == "q":
        break

    else:
        print ("Operação Inválida, por favor selecione novamente a operação desejada.")
