peso = float(input("Digite o seu peso (kg): "));
altura = float(input("Digite a sua altura (m): "));

IMC = peso / (altura ** 2);

if IMC < 18.5:
    print("Você está abaixo do peso.");
elif IMC < 25:
    print("Você está com o peso normal.");
elif IMC < 30:
    print("Você está com sobrepeso.");
else:
    print("Você está obeso.");
print(f"Seu IMC é: {IMC:.2f}");