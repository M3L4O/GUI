lista_de_usuarios = list()
def cadastrar(email, senha):
    lista_de_usuarios.append(usuario(email, senha))

def contains(email):
    for conta in lista_de_usuarios:
        if conta.email == email:
            return True
    return False

def autenticacao(email, senha):
    for conta in lista_de_usuarios:
        if conta.email == email:
            if conta.senha == senha:
                return True
            else:
                return False


class usuario:

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha