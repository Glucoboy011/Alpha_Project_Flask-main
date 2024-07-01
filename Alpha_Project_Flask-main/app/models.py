class Aluno:
    def __init__(self, nome, idade, serie, cpf, UF, cidade, github, linkedin, mini_bio, foto):
        self.nome = nome
        self.idade = idade
        self.serie = serie
        self.cpf = cpf
        self.uf = UF
        self.cidade = cidade
        self.github = github
        self.linkedin = linkedin
        self.mini_bio = mini_bio
        self.foto = foto

class Professor:
    def __init__(self, nome, idade, telefone, email, github, linkedin, bio, foto):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.github = github
        self.linkedin = linkedin
        self.bio = bio
        self.foto = foto
