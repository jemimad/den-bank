import unittest
import json

from server import app


class TestContaBonus(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def create_account(self, numero):
        payload = json.dumps({
            'numero': numero,
            'tipo': 2,
            'saldo': 0
        })
        self.app.post('/cadastro', headers={"Content-Type": "application/json"}, data=payload)

    def test_cadastro(self):
        payload = json.dumps({
            'numero': 7,
            'tipo': 2,
            'saldo': 0
        })

        response = self.app.post('/cadastro', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual('Conta bônus cadastrada com sucesso!', response.data.decode('utf-8'))
        self.assertEqual(201, response.status_code)

    def test_saldo(self):
        self.create_account(8)

        response = self.app.get(f'/saldo?numero={8}')

        self.assertEqual('0', response.data.decode('utf-8'))
        self.assertEqual(200, response.status_code)

    def test_deposito(self):
        self.create_account(9)

        payload = json.dumps({
            'numero': 9,
            'valor': 100
        })

        response = self.app.post('/deposito', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual('Depósito efetuado com sucesso!', response.data.decode('utf-8'))
        self.assertEqual(200, response.status_code)

    def test_saque(self):
        self.create_account(10)

        payload = json.dumps({
            'numero': 10,
            'valor': 100
        })

        response = self.app.post('/saque', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual('Saque efetuado com sucesso!', response.data.decode('utf-8'))
        self.assertEqual(200, response.status_code)

    def test_transferencia(self):
        self.create_account(11)
        self.create_account(12)
        self.app.post('/deposito', headers={"Content-Type": "application/json"}, data=json.dumps({'numero': 11, 'valor': 100}))

        payload = json.dumps({
            'numeroOrigem': 11,
            'numeroDestino': 12,
            'valor': 50
        })

        response = self.app.post('/transferencia', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual('Tranferência efetuada com sucesso!', response.data.decode('utf-8'))
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.TestLoader.sortTestMethodsUsing = lambda *args: -1
    unittest.main()
