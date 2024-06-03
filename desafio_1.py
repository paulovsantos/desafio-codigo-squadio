valor = float(input("Digite o valor de depósito: "))

if valor > 0:
    print(f"Deposito realizado com sucesso!" f"\nSaldo atual: R$ {valor:.2f}")
      
elif valor < 0:
    print("Valor invalido! Digite um valor maior que zero.")
    
else:
    print("Encerrando o programa...")
    