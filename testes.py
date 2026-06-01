import unittest
from datetime import datetime
from app import obter_resposta


class TestObterResposta(unittest.TestCase):

    def teste_saudacoes(self):
        """Teste de respostas a saudações - 3 testes"""
        self.assertEqual(obter_resposta("olá"), "Olá tudo bem!")
        self.assertEqual(obter_resposta("boa tarde"), "Olá tudo bem!")
        self.assertEqual(obter_resposta("bom dia"), "Olá tudo bem!")

    def teste_perguntas_simples(self):
        """Teste de respostas a perguntas simples - 4 testes"""
        self.assertEqual(obter_resposta("como estás"), "Estou bem, obrigado!")
        self.assertEqual(obter_resposta("como te chamas"), "O meu nome é Bot :)")
        self.assertEqual(obter_resposta("tempo"), "Está um dia de sol")
        self.assertEqual(obter_resposta("ajuda"), "Podes perguntar: horas, data, tempo, como estás, e meu nome")

    def teste_despedidas(self):
        """Teste de respostas a despedidas - 3 testes"""
        self.assertEqual(obter_resposta("bye"), "Gostei de falar contigo! Até breve...")
        self.assertEqual(obter_resposta("adeus"), "Gostei de falar contigo! Até breve...")
        self.assertEqual(obter_resposta("tchau"), "Gostei de falar contigo! Até breve...")

    def teste_horas_e_data(self):
        """Teste de respostas a perguntas sobre horas e data"""
        hora_atual = datetime.now().strftime("%H:%M")
        data_atual = datetime.now().strftime("%d-%m-%Y")
        self.assertEqual(obter_resposta("que horas são"), f"São: {hora_atual} horas")
        self.assertEqual(obter_resposta("qual é a data"), f"Hoje é dia: {data_atual}")

    def teste_resposta_padrao(self):
        """Teste de resposta padrão - 3 testes"""
        self.assertEqual(obter_resposta("xyz123"), "Desculpa, não entendi a questão! xyz123")
        self.assertEqual(obter_resposta("teste123"), "Desculpa, não entendi a questão! teste123")
        self.assertEqual(obter_resposta("abcdef"), "Desculpa, não entendi a questão! abcdef")


if __name__ == '__main__':
    unittest.main()