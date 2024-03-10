import unittest


def fatorial(n):
    if n < 0:
        raise ValueError(
            "Não é possível calcular o fatorial de um número negativo.")
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n+1):
            resultado *= i
        return resultado


class TestFatorial(unittest.TestCase):

    def test_fatorial_positivo(self):
        # Teste para um número positivo
        resultado = fatorial(5)
        self.assertEqual(resultado, 120)  # 5! = 120

    def test_fatorial_negativo(self):
        # Teste para um número negativo (deve levantar uma exceção)
        with self.assertRaises(ValueError):
            fatorial(-5)


if __name__ == '__main__':
    unittest.main()
