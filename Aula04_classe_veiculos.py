qnt_rodas = int(input("Insira a quantidade de rodas do veículo:"))
peso_kg = float(input("Insira o peso bruto do veículo em quilogramas:"))
qnt_pessoas = int(input("Insira a quantidade de pessoas no veículo:"))

if qnt_rodas >=2 and qnt_rodas <=3:
    print("É um veículo da classe A.")
elif qnt_rodas == 4 and qnt_pessoas <= 8 and peso_kg <= 3500:
    print("É um veículo da classe B.")
elif qnt_rodas >= 4 and peso_kg >= 3500 and peso_kg <= 6000:
    print("É um veículo da classe C.")
elif qnt_rodas >= 4 and qnt_pessoas >= 8 or qnt_rodas >= 4 and peso_kg > 6000:
    print("É um veículo de classe D.")