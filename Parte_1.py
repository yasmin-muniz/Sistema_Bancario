menu = """


[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """


saldo = 1000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor_saque = 0
dict_saque = {}
lista_extrato = []
valor_deposito = 0


while True:
    

    opcao = input (menu)

    if opcao == "d": 
        valor_deposito =  int(input ('Qual valor a ser depositado?')) 
        saldo += valor_deposito 
        lista_extrato.append(f'Depósito: R$ {valor_deposito}')
    
    elif opcao == "s":
        valor_saque = int(input ('Qual valor a ser sacado?')) 
        if valor_saque > limite:
           print ("O limite para saque é de R$500,00 reais") 
        elif valor_saque > saldo:
            print("Não há saldo suficiente na conta!")
        elif numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite de saques diários!") 
        else:
            saldo -= valor_saque
            lista_extrato.append(f'Saque: R$ {valor_saque}')  
            numero_saques += 1
            print(f"Saque de R${valor_saque} realizado com sucesso!")

    
    elif opcao == "e": 
        for transacao in lista_extrato:
            print(transacao)
        print(f"Saldo: R${saldo}")
    
    elif opcao == "q":
        break

    else:
        print ("Operação Inválida, por favor selecione novamente a operação desejada.")
