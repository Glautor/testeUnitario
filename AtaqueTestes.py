from Jogo import Jogo
from Monstro import *
from Ataque import *
from Jogador import *
from random import randint
import unittest

class AtaqueTestes(unittest.TestCase):
    def teste_acertou_arma_givenRespostaCorreta_whenAcertouArma_then_ArmasCorretasNaPosicaoErrada(self):
        #given
        self.ataque = AtaqueStub([1, 2, 5, 4])
        randomNumber = randint(1, 9)

        #when
        for i in range(randomNumber):
            self.ataque.acertouArma()

        #then
        self.assertEqual(self.ataque.armasCorretasNaPosicaoErrada, randomNumber)

    def teste_acertou_arma_givenRespostaCorreta_whenAcertouArma_then_ArmasCorretasNaPosicaoErrada(self):
        #given
        self.ataque = AtaqueStub([1, 2, 5, 4])
        randomNumber = randint(1, 9)

        #when
        for i in range(randomNumber):
            self.ataque.acertouArma()

        #then
        self.assertEqual(self.ataque.armasCorretasNaPosicaoErrada, randomNumber)

    def teste_conferir_se_ganhou_givenArmasCorretasNaPosicaoCorreta4Vezes_whenConferirSeGanhou_then_RetornaVerdadeiro(self):
        #given
        self.ataque = AtaqueStub([1, 2, 5, 4])
        self.ataque.acertouAtaque()
        self.ataque.acertouAtaque()
        self.ataque.acertouAtaque()
        self.ataque.acertouAtaque()

        #when
        conferirSeGanhou = self.ataque.conferirSeGanhou()

        #then
        self.assertTrue(conferirSeGanhou)

    def teste_conferir_se_ganhou_givenArmasCorretasNaPosicaoCorretaDiferenteDe4Vezes_whenConferirSeGanhou_then_RetornaFalso(self):
        #given
        randomNumber = randint(0, 3)
        self.ataque = AtaqueStub([1, 2, 5, 4])

        for i in range(randomNumber):
            self.ataque.acertouAtaque()

        #when
        conferirSeGanhou = self.ataque.conferirSeGanhou()

        #then
        self.assertFalse(conferirSeGanhou)

if __name__ == '__main__':
    unittest.main(verbosity=2)
