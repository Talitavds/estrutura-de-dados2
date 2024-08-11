class Node:
    def __init__(self, data=None):
        self.data = data
        self.proximo = None

class LinkedList:
    def __init__(self):
        self.elemento = None

    def append(self, data):
        novo_no = Node(data)
        if self.elemento is None:
            self.elemento = novo_no
            return
        ultimo_no = self.elemento
        while ultimo_no.proximo:
            ultimo_no = ultimo_no.proximo
        ultimo_no.proximo = novo_no

    def find(self, chave):
        atual = self.elemento
        while atual:
            if atual.data == chave:
                return atual
            atual = atual.proximo
        return None

    def remove(self, chave):
        atual = self.elemento
        if atual and atual.data == chave:
            self.elemento = atual.proximo
            atual = None
            return
        anterior = None
        while atual and atual.data != chave:
            anterior = atual
            atual = atual.proximo
        if atual is None:
            return
        anterior.proximo = atual.proximo
        atual = None

    def display(self):
        nodes = []
        atual = self.elemento
        while atual:
            nodes.append(atual.data)
            atual = atual.proximo
        return nodes

    def busca(self, chave):
        node = self.find(chave)
        return node.data if node else 'Não encontrado'
    
def executar(): 
    ll = LinkedList()

    for i in range(1, 11):
        ll.append(i)

    print("Lista após adições:", ll.display())

    for i in range(10):
        print(f"Encontrando elemento {i}:", ll.busca(i), '\t',ll.find(i))

    for i in range(6):
        if ll.find(i) is not None:
            ll.remove(i)
            print(f"Lista após remover {i}:", ll.display())
        else:
            print(f"Lista após tentar remover {i} (inexistente):", ll.display())
executar()