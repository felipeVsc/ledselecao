import csv

def faltaDados(contador):
    listaCat = ['first_name', 'last_name', 'company_name', 'address', 'city', 'county', 'state', 'zip', 'phone1', 'phone2', 'email', 'web']
    
    for x in range(12):
            if(contador!=0):
                if(linha[x]=="" or linha[x]==" " or linha[x]=='""' or linha[x]=='" "'):
                    print("Dado faltando na categoria",listaCat[x],"no usuario de numero",contador-1,"com first_name e last_name",linha[0],linha[1])
                    

with open('us-500.csv') as ficheiro:
    reader = csv.reader(ficheiro)
    contador = 0
    for linha in reader:
        faltaDados(contador)
        contador+=1
