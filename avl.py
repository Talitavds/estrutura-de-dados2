import time
import os
import pandas as pd

class No:
    def __init__(self, chave=None):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1

class AVL:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = No(chave)
        else:
            self.raiz = self._inserir(self.raiz, chave)

    def _inserir(self, no_atual, chave):
        if no_atual is None:
            return No(chave)

        if chave < no_atual.chave:
            no_atual.esquerda = self._inserir(no_atual.esquerda, chave)
        else:
            no_atual.direita = self._inserir(no_atual.direita, chave)

        no_atual.altura = 1 + max(self._get_altura(no_atual.esquerda), self._get_altura(no_atual.direita))

        balanceamento = self._get_balanceamento(no_atual)

        # Rotação à direita
        if balanceamento > 1 and chave < no_atual.esquerda.chave:
            return self._rotacao_direita(no_atual)

        # Rotação à esquerda
        if balanceamento < -1 and chave > no_atual.direita.chave:
            return self._rotacao_esquerda(no_atual)

        # Rotação dupla à direita
        if balanceamento > 1 and chave > no_atual.esquerda.chave:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        # Rotação dupla à esquerda
        if balanceamento < -1 and chave < no_atual.direita.chave:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        return no_atual

    def remover(self, chave):
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, no_atual, chave):
        if no_atual is None:
            return no_atual

        if chave < no_atual.chave:
            no_atual.esquerda = self._remover(no_atual.esquerda, chave)
        elif chave > no_atual.chave:
            no_atual.direita = self._remover(no_atual.direita, chave)
        else:
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda
            no_novo = self._encontrar_minimo(no_atual.direita)
            no_atual.chave = no_novo.chave
            no_atual.direita = self._remover(no_atual.direita, no_novo.chave)

        if no_atual is None:
            return no_atual

        no_atual.altura = 1 + max(self._get_altura(no_atual.esquerda), self._get_altura(no_atual.direita))

        balanceamento = self._get_balanceamento(no_atual)

        # Rotação à direita
        if balanceamento > 1 and self._get_balanceamento(no_atual.esquerda) >= 0:
            return self._rotacao_direita(no_atual)

        # Rotação à esquerda
        if balanceamento < -1 and self._get_balanceamento(no_atual.direita) <= 0:
            return self._rotacao_esquerda(no_atual)

        # Rotação dupla à direita
        if balanceamento > 1 and self._get_balanceamento(no_atual.esquerda) < 0:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        # Rotação dupla à esquerda
        if balanceamento < -1 and self._get_balanceamento(no_atual.direita) > 0:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        return no_atual

    def _rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda

        y.esquerda = z
        z.direita = T2

        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))

        return y

    def _rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita

        y.direita = z
        z.esquerda = T3

        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))

        return y

    def _get_altura(self, no):
        if no is None:
            return 0
        return no.altura

    def _get_balanceamento(self, no):
        if no is None:
            return 0
        return self._get_altura(no.esquerda) - self._get_altura(no.direita)

    def _encontrar_minimo(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def percurso_em_ordem(self):
        elementos = []
        self._percurso_em_ordem(self.raiz, elementos)
        return elementos

    def _percurso_em_ordem(self, no, elementos):
        if no:
            self._percurso_em_ordem(no.esquerda, elementos)
            elementos.append(no.chave)
            self._percurso_em_ordem(no.direita, elementos)

    def buscar(self, chave):
        return self._buscar(self.raiz, chave)

    def _buscar(self, no_atual, chave):
        if no_atual is None or no_atual.chave == chave:
            return no_atual
        if chave < no_atual.chave:
            return self._buscar(no_atual.esquerda, chave)
        return self._buscar(no_atual.direita, chave)
def executar():
    avl = AVL()

    for chave in [20, 10, 30, 5, 15, 25, 35, 2, 6, 45]:
        avl.inserir(chave)

    print(f'AVL após incerção (percurso em ordem):\t{avl.percurso_em_ordem()}')

#user = int(input('Digite um número para a remoção:\t'))
    user = 10
    avl.remover(user)
    print(f'AVL após remover {user} (percurso em ordem): {avl.percurso_em_ordem()}')


#user = int(input('Digite um número para a busca:\t'))

# CASO AFIRMATIVO

    user = 15
    print(f'Elemento {user}:', 'Encontrado' if avl.buscar (user) else 'Não encontrado')

# CASO NEGATIVO

    user = 10
    print(f'Elemento {user}:', 'Encontrado' if avl.buscar (user) else 'Não encontrado')

executar()
