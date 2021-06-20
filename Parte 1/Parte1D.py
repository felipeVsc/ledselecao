import csv
   
def novoFormatoEndereco(entrada):
    
    novaLista = entrada.split(" ")
    novoEndereco = []
    controle = ""
    for x in range(len(novaLista)):
        if(x==0):
            novoEndereco.append(novaLista[x])

        else:
            if(x==len(novaLista)-1):
                novoEndereco.append(controle)
                if(novaLista[x][0]=="#"):
                    novoEndereco.append(novaLista[x])
                else:
                     novoEndereco.append(" ")
            else:
                controle+=novaLista[x]
                controle+=" "
    return novoEndereco

def substituirEndereco(reader):
        contador = 0
        for linha in reader:
            if(contador!=0):   
                linha[3] = novoFormatoEndereco(linha[3])
                print(linha[3])
                contador+=1
            else:
                contador+=1

with open('us-500.csv') as ficheiro:
    reader = csv.reader(ficheiro)
    substituirEndereco(reader)