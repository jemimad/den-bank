import unittest
import json

from server import app


class TestContaSimples(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def create_account(self, numero):
        payload = json.dumps({
            'numero': numero,
            'tipo': 1,
            'saldo': 0
        })
        self.app.post('/cadastro', headers={"Content-Type": "application/json"}, data=payload)

    def test_cadastro(self):
        payload = json.dumps({
            'numero': 1,
            'tipo': 1,
            'saldo': 0
        })

        response = self.app.post('/cadastro', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual('Conta simples cadastrada com sucesso!', response.data.decode('utf-8'))
        self.assertEqual(201, response.status_code)

    def test_saldo(self):
        self.create_account(2)

        response = self.app.get(f'/saldo?numero={2}')

        self.assertEqual('0', response.data.decode('utf-8'))
        self.assertEqual(200, response.status_code)

    def test_deposito(self):
        self.create_account(3)

        payload = json.dumps({
            'numero': 3,
            'valor': 100
        })

        response = self.app.post('/deposito', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual('Depósito efetuado com sucesso!', response.data.decode('utf-8'))
        self.assertEqual(200, response.status_code)

    def test_saque(self):
        self.create_account(4)

        payload = json.dumps({
            'numero': 4,
            'valor': 100
        })

        response = self.app.post('/saque', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual('Saque efetuado com sucesso!', response.data.decode('utf-8'))
        self.assertEqual(200, response.status_code)

    def test_transferencia(self):
        self.create_account(5)
        self.create_account(6)
        self.app.post('/deposito', headers={"Content-Type": "application/json"}, data=json.dumps({'numero': 5, 'valor': 100}))

        payload = json.dumps({
            'numeroOrigem': 5,
            'numeroDestino': 6,
            'valor': 50
        })

        response = self.app.post('/transferencia', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual('Tranferência efetuada com sucesso!', response.data.decode('utf-8'))
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.TestLoader.sortTestMethodsUsing = lambda *args: -1
    unittest.main()
