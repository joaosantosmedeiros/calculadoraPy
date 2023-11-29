import unittest
from emprestimo_calculator import EmprestimoCalculator
from app import validar_dados

class TestEmprestimoCalculator(unittest.TestCase):
    def test_calcular_limite_parcela(self):
        self.assertEqual(EmprestimoCalculator.calcular_limite_parcela(1000), 300)

    def test_calcular_pagamento_mensal(self):
        self.assertAlmostEqual(
            EmprestimoCalculator.calcular_pagamento_mensal(1000, 12),
            88.85,
            places=2
        )

    def test_calcular_valor_max_cedido(self):
        self.assertAlmostEqual(
            EmprestimoCalculator.calcular_valor_max_cedido(300, 0.01, 12),
            3376.52,
            places=2
        )

    def test_aprovar_emprestimo(self):
        self.assertTrue(EmprestimoCalculator.aprovar_emprestimo(100, 200))
        self.assertFalse(EmprestimoCalculator.aprovar_emprestimo(300, 200))

    def test_validar_dados(self):
        self.assertFalse(validar_dados(-1, 400, 12))
        self.assertFalse(validar_dados(1, 99, 12))
        self.assertFalse(validar_dados(1, 100, 0))
        self.assertFalse(validar_dados(1, 100, 97))
        self.assertTrue(validar_dados(1, 100, 12))

if __name__ == '__main__':
    unittest.main()
