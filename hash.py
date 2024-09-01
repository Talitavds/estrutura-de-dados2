class Contato:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __repr__(self):
        return f"Contato(nome={self.nome}, email={self.email})"

class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _funcao_hash(self, email):
        return sum(ord(char) for char in email) % self.tamanho

    def inserir(self, nome, email):
        indice = self._funcao_hash(email)
        for contato in self.tabela[indice]:
            if contato.email == email:
                contato.nome = nome
                return
        self.tabela[indice].append(Contato(nome, email))

    def buscar(self, email):
        indice = self._funcao_hash(email)
        for contato in self.tabela[indice]:
            if contato.email == email:
                return contato
        return None

    def remover(self, email):
        indice = self._funcao_hash(email)
        bucket = self.tabela[indice]
        for i, contato in enumerate(bucket):
            if contato.email == email:
                del bucket[i]
                return True
        return False

    def __repr__(self):
        return '\n'.join(f"Bucket  {i}: {bucket}" for i, bucket in enumerate(self.tabela))

if __name__ == "__main__":
    tabela_hash = TabelaHash(tamanho=10)

    tabela_hash.inserir("Tartaruga", "tartaruga@iffar.com")
    tabela_hash.inserir("Cao", "cao@iffar.com")
    tabela_hash.inserir("Passaro", "passaro@iffar.com")
    tabela_hash.inserir("Gato", "gato@iffar.com")
    tabela_hash.inserir("Galinha", "galinha@iffar.com")
    tabela_hash.inserir("Pato", "pato@iffar.com")
    tabela_hash.inserir("Avestruz", "avestruz@iffar.com")
    tabela_hash.inserir("Boi", "boi@iffar.com")
    tabela_hash.inserir("Vaca", "vaca@iffar.com")
    tabela_hash.inserir("Ovelha", "ovelha@iffar.com")

    print(f'Busca por pato@iffar.com: \t{tabela_hash.buscar("pato@iffar.com")}')
    print(f'Busca por galinha@iffar.com: \t{tabela_hash.buscar("galinha@iffar.com")}')

    print(f'Valor pato@iifar.com removido: \t{tabela_hash.remover("pato@iffar.com")}')
    print(f'Busca por pato@iffar.com: \t{tabela_hash.buscar("pato@example.com")}')

    print(f'\n{tabela_hash}')

'''
# Teste de id
email = "tartaruga@iffar.com"
indice = sum(ord(char) for char in email) % 10
print (email, indice)
'''