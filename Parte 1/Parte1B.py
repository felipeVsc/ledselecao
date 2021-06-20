import csv

states = ["AK","AL","AR","AS","AZ","CA","CO","CT","DC","DE","FL","GA","GU","HI","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VA","VI","VT","WA","WI","WV","WY"]

def printarBlocos(estadoNum):
    with open('us-500.csv') as ficheiro:
        reader = csv.reader(ficheiro)
        for linha in reader:
            if(linha[6]==states[estadoNum]):
                print(linha[6],"      ",linha[3])
 
for x in range(len(states)):
    printarBlocos(x)
    


    