import json
agenda=[]
x=input("Nome: ")
telefone=input("Telefone: ")
contato={"nome": x, telefone: '111-222'}

agenda.append(contato)

for item in agenda:
    for chaves, valores in item.items():
        print("chaves", valores)
        print("Valores:", valores)

saida = json.dumps(agenda)

agenda2 = json.loads(saida)

for item in agenda2:
    for chaves, valores in item.items():
        print("chave: ", chaves)
        print("Valor:",valores)

with open("teste.json", 'w') as file: 
    json.dump(, file, indent=4)

