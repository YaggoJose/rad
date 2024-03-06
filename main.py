'''arquivo = open("texto.txt","r")'''


'''print(arquivo.readline())
print(arquivo.readline())
print(arquivo.seek(0))
print(arquivo.readlines())
print(arquivo.seek(0))'''
'''print(arquivo.tell())
print(arquivo.close())
print(arquivo.closed)'''


'''arquivo = open("novo.txt", "w")
arquivo.write("arquivo de escrita")
arquivo.close()
print(arquivo.closed)'''


'''arquivo = open("frutas.txt","w")
arquivo.write("banana")
arquivo.write("uva")
arquivo.write("mamao")
arquivo.close()'''

'''precos = [20,100,500,600]
with open ("precos_roupas.txt","w") as arquivo:
 for preco in precos:
    arquivo.write(str(preco) + '\n')
print(arquivo.closed)'''

'''precos = [8000]
with open("precos_roupas.txt","a") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')'''

'''precos = [100000]
with open("precos_roupas", "w") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')'''


'''disciplinas = ["rad \n, introdução a C \n", "programação 1 \n "]
with open("disciplinas.txt", "w") as file:
    file.write("Relação de disciplinas \n")
    file.writelines(disciplinas)

with open("disciplinas.txt" ,"r") as file:
    print(file.read())'''

'''with open("texto.txt", "r") as arquivo:
    print("representação original da linha")
    for linha in arquivo:
        print(repr(linha))

with open("texto,txt", "r") as arquivo:
    print("conteudo da linha")
    for linha in arquivo:
        linha_ = linha.strip()
        print(repr(linha_))'''

'''minha_lista = ["arroz", "feijao", "carne"]
lista_ = '.'.join(minha_lista)
with open("texto_.txt","w") as arquivo:
    arquivo.write(lista_)'''


'''try:
    with open("arquivo_text.txt", "r") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("arquivo inexistente")'''

'''import os 
try:
    os.remove("teste.txt")
    print("Arquivo foi removido")
except FileNotFoundError as erro:
    print("arquivo inexistente")
    print("descrição", erro) '''

'''try:
    f = open("novo2.txt","r")
    f.write("hello")
except IOError as erro:
    print("O erro foi", erro)'''


with open("notas.txt", "w") as f:
    for nome.nota in notas:
        f.write(f"nome:{nome}, Nota:{nota}\n")


with open("notas.txt", "r") as f:
    for linha in f:
        print(f.seek(0))
        print(f.read())

try:
    with open("novas_notas" , "r") as arquivo:
        arquivo.read
except FileNotFoundError:
    print("aquivo inexistente")

try:
    open("notas.txt", "r") as arquivo:
    arquivo.writelines(['Yaggo.10,10'])
except IOError:
        print("sem permissão")