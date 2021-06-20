import mysql.connector

class conexaoBanco():
    def __init__(self):
        try:
            self.banco = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="12345678",
                    database="banco"
                )
        except:
            # Nao existe o banco de dados, logo criar ele
            banco = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345678"
            )
            cursorBanco = banco.cursor()
            cursorBanco.execute("CREATE DATABASE banco")
        finally:
            self.criarTabelas()

    def criarTabelas(self):
    
        try:
            banco = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345678",
                database="banco"
            )
            cursorBanco = banco.cursor()
            cursorBanco.execute("CREATE TABLE pacientes (paciente_id VARCHAR(50) PRIMARY KEY, paciente_datanascimento DATE,paciente_enumsexobiologico CHAR, paciente_racacor_codigo INT, paciente_racacor_valor VARCHAR(20),paciente_endereco_coibgemunicipio INT, paciente_endereco_copais INT,paciente_endereco_nmmunicipio VARCHAR(50),paciente_endereco_nmpais VARCHAR(50),paciente_endereco_uf VARCHAR(2),paciente_endereco_cep INT,paciente_nacionalidade_enumnacionalidade CHAR)")

            cursorBanco.execute("CREATE TABLE vacina(paciente_id VARCHAR(50) PRIMARY KEY, vacina_grupoatendimento_codigo INT, vacina_grupoatendimento_nome VARCHAR(50),vacina_categoria_codigo INT,vacina_categoria_nome VARCHAR(50),vacina_lote VARCHAR(50),vacina_fabricante_nome VARCHAR(50),vacina_fabricante_referencia VARCHAR(50),vacina_dataaplicacao DATE,vacina_descricao_dose VARCHAR(50),vacina_codigo INT,vacina_nome VARCHAR(50))")

            cursorBanco.execute("CREATE TABLE estabelecimento(paciente_id VARCHAR(50) PRIMARY KEY,estabelecimento_valor INT,estabelecimento_razaosocial VARCHAR(50),estalecimento_nofantasia VARCHAR(50),estabelecimento_municipio_codigo INT,estabelecimento_municipio_nome VARCHAR(50),estabelecimento_uf VARCHAR(2))")
            print("Tabelas criadas")
        except:
            print("Tabelas já existem")
            
    def getCursor(self):
        return self.banco.cursor()