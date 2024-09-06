nome=input("Digite o seu nome: ")
idade=int(input("Digite a sua idade: "))
peso=float(input("Digite o seu peso (em kg): "))
altura=float(input("Digite a sua altura (em metros): "))
IMC = peso / (altura ** 2)

if IMC<18.5:
    classificacao="Magro"
elif IMC<24.9:
    classificacao="Ta maneiro"
elif IMC<29.9:
    classificacao="Gordinho"
elif IMC<34.9:
    classificacao="Gordo"
elif IMC<39.9:
    classificacao="Gordão"
else:
    classificacao="Thais Carla"

print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Peso: {peso:.2f} kg")
print(f"Altura: {altura:.2f} m")
print(f"IMC: {IMC:.2f}")
print(f"Classificação: {classificacao}")


ass: alyssiNN
ass: thigas
             
