import unittest
from calculadora import calcular_porcentagens, escalonar_receita, validar_receita

class TestCalculadoraPanificacao(unittest.TestCase):

    # Teste 1: Matemática base
    def test_calculo_porcentagem(self):
        dados = {"farinha": 1000, "agua": 700}
        resultado = calcular_porcentagens(dados)
        self.assertEqual(resultado["agua"], 70)

    # Teste 2: Escalonamento (Corrigido: removido o 'nome,')
    def test_escalonar_italiano(self):
        resultado = escalonar_receita(1000) 
        self.assertEqual(resultado["agua"], 700)

    # Teste 3: Hidratação segura
    def test_validar_sucesso(self):
        receita = {"farinha": 500, "agua": 300}
        msg = validar_receita(receita)
        self.assertIn("✅", msg)

    # Teste 4: Alerta de massa mole
    def test_validar_alerta(self):
        receita = {"farinha": 500, "agua": 450}
        msg = validar_receita(receita)
        self.assertIn("⚠️", msg)

    # Teste 5: Proporção de Sal (Corrigido: removido o '_,')
    def test_escalonamento_sal(self):
        resultado = escalonar_receita(250)
        self.assertEqual(resultado["sal"], 5.0)

if __name__ == '__main__':
    unittest.main()