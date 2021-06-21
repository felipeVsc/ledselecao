with open('parte3vac1.csv', 'r') as t1, open('parte3vac2.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

def matchAndHasAlteracoes(newdados,fileone):
    for line2 in fileone:
        newdados2 = line2.split(';')
        if(newdados[0]==newdados2[0] and newdados[0]!='"document_id"' and newdados2[0]!='"document_id"'):
            print("DOCID Match",newdados2[0])
            soma = 0
            for x in range(34):
                if(newdados[x]==newdados2[x]):
                    soma+=1
                else:
                    pass
            if(soma==34):
                print("Sem alteracoes")
                soma = 0
            else:
                print("Alteracoes ocorreram")
                soma = 0
        else:
            pass


for line in filetwo:
    newdados = line.split(";")
    matchAndHasAlteracoes(newdados,fileone)