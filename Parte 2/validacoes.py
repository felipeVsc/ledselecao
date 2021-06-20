class Validacoes:

    def __init__(self, newdados):
        self.newdados = newdados

    def validacaoDadosEmBranco(self):
        categorias = ["document_id","paciente_id","paciente_idade","paciente_datanascimento","paciente_enumsexobiologico","paciente_racacor_codigo","paciente_racacor_valor","paciente_endereco_coibgemunicipio","paciente_endereco_copais","paciente_endereco_nmmunicipio","paciente_endereco_nmpais","paciente_endereco_uf","paciente_endereco_cep","paciente_nacionalidade_enumnacionalidade","estabelecimento_valor","estabelecimento_razaosocial","estalecimento_nofantasia","estabelecimento_municipio_codigo","estabelecimento_municipio_nome","estabelecimento_uf","vacina_grupoatendimento_codigo","vacina_grupoatendimento_nome","vacina_categoria_codigo","vacina_categoria_nome","vacina_lote","vacina_fabricante_nome","vacina_fabricante_referencia","vacina_dataaplicacao","vacina_descricao_dose","vacina_codigo","vacina_nome","sistema_origem","data_importacao_rnds","id_sistema_origem"]
        for x in range(0,33):  
            if(self.newdados[x]=='""'):
                print("DADOS INCOMPLETOS DO DOCID:",self.newdados[0],"CATEGORIA: ",categorias[x])

    def validarIdades(self):
        idadeListas = self.newdados[2].split('"')
        if(idadeListas[1]!="paciente_idade"):
            idadeInteiro = int(idadeListas[1])
            if(idadeInteiro<14 or idadeInteiro>130):
                if(self.newdados[23]=='"Faixa Etária"' or self.newdados[23]=='""' or self.newdados[23]=='"Trabalhadores de Saúde"'):
                    print("Idade errada no DOCID",self.newdados[0]," GRUPO:",self.newdados[23])


    def validarDataNascimento(self):
        datasListas = self.newdados[3].split('"')
        if(datasListas[1]!="paciente_datanascimento"):
            datasSeparadas = datasListas[1].split("-")
            ano = int(datasSeparadas[0])
            mes = int(datasSeparadas[1])
            dia = int(datasSeparadas[2])

            if(ano<1891 or ano>2021 or mes>12 or mes<1 or dia>31 or dia<1):
                print("DATA DE NASCIMENTO INVALIDA - DOCID",self.newdados[0])
            

    