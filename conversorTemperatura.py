valor = float(input("Digite a temperatura a ser convertida: "));
origem = input("Digite a unidade de origem (Celsius, Fahrenheit, Kelvin): ");
destino = input("Digite a unidade de destino (Celsius, Fahrenheit, Kelvin): ");

if origem == "Celsius":
    Celsius = valor;
elif origem == "Fahrenheit":
    Celsius = (valor - 32) * 5/9;
elif origem == "Kelvin":
    Celsius = valor - 273.15;

if destino == "Celsius":
    resultado = Celsius;
elif destino == "Fahrenheit":
    resultado = Celsius * 9/5 + 32;
elif destino == "Kelvin":
    resultado = Celsius + 273.15;

print(f"{valor} {origem.capitalize()} equivale a {resultado:.2f}");