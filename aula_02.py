class Endereco():
    def __init__(self,rua=None,lote=None,quadra=None):
        self.rua=rua
        self.lote=lote
        self.quadra=quadra
    def __str__(self):
        return self.rua+','+self.lote+','+self.quadra
class Pessoa():
    
    def __init__(self,nome=None,data_nascimento=None,endereco=None):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco=endereco
    def __str__(self):
        return self.cpf+','+self.nome+','+self.data_nascimento+','self.Endereco)

class PessoaFisica(Pessoa):

    def __init__(self,cpf=None,nome=None,data_nascimento=None,endereco=None):
        Pessoa.__init__(self,nome,data_nascimento,endereco)
        self.cpf = cpf

class PessoaJuridica(Pessoa):
    def __init__(self,cnpj=None,nome=None,data_nascimento=None):
        Pessoa.__init__(self,nome,data_nascimento,endereco)
        self.cnpj =cnpj

nome=PessoaFisica('01350020109','claison','29/01/1988',Endereco('Rua jorge Barroca','20','38'))
print(nome)
