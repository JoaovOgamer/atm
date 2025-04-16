#Fazer um sistema de banco
#Precisa ter saque, deposito e checar saldo

saldo = 100

while True:

    print("Bem vindo ao banco batata")
    print("Escolha uma opçao")

    print("1 - Saque")
    print("2 - Checar saldo")
    print("3 - Depositar")
    print("4 - sair")

    answer = int(input("Opção:"))

    if answer == 1:
        question = int(input("Quanto você gostaria de sacar"))
        if saldo > question: 
            saldo -= question
    elif answer == 2:
        print(saldo)
    elif answer == 3:
         question = int(input("Quanto você gostaria de depositar"))
         saldo += question
    elif answer == 4:
        print("Adeus")
        break

    