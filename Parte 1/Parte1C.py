import csv
def validarZipCode(entrada):
    if(len(entrada)==5 and entrada.isdigit()):
        return True
    return False

def rodarValidacao(reader):
    
        contador = 0
        for linha in reader:
            if(validarZipCode(linha[7])==False and contador!=0):
                print("Erro")
            contador+=1
            
with open('us-500.csv') as ficheiro:
        reader = csv.reader(ficheiro)
        rodarValidacao(reader)
