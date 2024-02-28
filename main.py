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

'''preco = [20,100,500,600]
with open ("precos_roupas.txt","w") as arquivo:
 for preco in precos:
    arquivo.write(str(preco)+ '/n')
print(arquivo.closed)'''

'''preco = [8000]
with open("precos_roupas.txt","a") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) +'/n')'''

