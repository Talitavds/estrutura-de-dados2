class No:
    def __init__ (self, chave=None):
        self.chave = chave
        self.esquerda = None
        self.direita =None

class ABB:
    def __init__(self):
        self.raiz = None

    def inserir (self, chave):
        if self.raiz is None:
            self.raiz = No(chave)
        else:
            self._inserir(self.raiz, chave)

    def _inserir(self, no_atual, chave):
        if chave < no_atual.chave:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(chave)
            else:
                self._inserir(no_atual.esquerda, chave)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(chave)
            else:
                self._inserir(no_atual.direita, chave)

    def buscar(self, chave):
        return self._buscar(self.raiz,chave)
    
    def _buscar(self, no_atual, chave):
        if no_atual is None or no_atual.chave == chave:
            return no_atual
        if chave < no_atual.chave:
            return self._buscar(no_atual.esquerda, chave)
        return self._buscar(no_atual.direita, chave)
    
    def remover (self, chave):
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, no_atual, chave):
        if no_atual is None:
            return no_atual
        if chave < no_atual.chave:
            no_atual.esquerda =self._remover(no_atual.esquerda, chave)
        elif chave> no_atual.chave:
            no_atual.direita = self._remover(no_atual.direita, chave)
        else:
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esauerda
            no_novo = self._encontrar_minimo(no_atual.direita)
            no_atual.chave = no_novo.chave
            no_atual.direita = self._remover(no_atual.direita, no_novo.chave)
        return no_atual
    
    def _encontrar_minimo (self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual
    
    def percurso_em_ordem(self):
        elementos =[]
        self._percurso_em_ordem(self.raiz, elementos)
        return elementos
    
    def _percurso_em_ordem(self, no, elementos):
        if no:
            self._percurso_em_ordem(no.esquerda, elementos)
            elementos.append(no.chave)
            self._percurso_em_ordem(no.direita, elementos)
def executar():
    abb = ABB()

    for chave in [20, 10, 30, 5, 15, 25, 35, 2, 6, 45]:
        abb.inserir(chave)

    print(f'ABB após incerção (percurso em ordem):\t{abb.percurso_em_ordem()}')

#user = int(input('Digite um número para a remoção:\t'))
    user = 10
    abb.remover(user)
    print(f'ABB após remover {user} (percurso em ordem): {abb.percurso_em_ordem()}')


#user = int(input('Digite um número para a busca:\t'))

# CASO AFIRMATIVO

    user = 15
    print(f'Elemento {user}:', 'Encontrado' if abb.buscar (user) else 'Não encontrado')

# CASO NEGATIVO

    user = 10
    print(f'Elemento {user}:', 'Encontrado' if abb.buscar (user) else 'Não encontrado')

executar()