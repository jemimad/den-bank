import unittest
import json

from server import app

class TestContaPoupanca(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def create_account(self, numero, saldo=0):
        payload = json.dumps({
            'numero': numero,
            'tipo': 3,
            'saldo': saldo
        })
        self.app.post('/cadastro', headers={"Content-Type": "application/json"}, data=payload)

    def test_cadastro(self):
        payload = json.dumps({
            'numero': 13,
            'tipo': 3,
            'saldo': 10
        })

        response = self.app.post('/cadastro', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual('Conta poupança cadastrada com sucesso!', response.data.decode('utf-8'))
        self.assertEqual(201, response.status_code)

    def test_saldo(self):
        self.create_account(14)

        response = self.app.get(f'/saldo?numero={14}')

        self.assertEqual('0', response.data.decode('utf-8'))
        self.assertEqual(200, response.status_code)

    def test_deposito(self):
        self.create_account(15)

        payload = json.dumps({
            'numero': 15,
            'valor': 100
        })

        response = self.app.post('/deposito', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual('Depósito efetuado com sucesso!', response.data.decode('utf-8'))
        self.assertEqual(200, response.status_code)

    def test_saque(self):
        self.create_account(16, 100)

        payload = json.dumps({
            'numero': 16,
            'valor': 50
        })

        response = self.app.post('/saque', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual('Saque efetuado com sucesso!', response.data.decode('utf-8'))
        self.assertEqual(200, response.status_code)

    def test_transferencia(self):
        self.create_account(17)
        self.create_account(18)
        self.app.post('/deposito', headers={"Content-Type": "application/json"}, data=json.dumps({'numero': 17, 'valor': 100}))

        payload = json.dumps({
            'numeroOrigem': 17,
            'numeroDestino': 18,
            'valor': 50
        })

        response = self.app.post('/transferencia', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual('Tranferência efetuada com sucesso!', response.data.decode('utf-8'))
        self.assertEqual(200, response.status_code)

    def test_render_juros(self):
        self.create_account(19, 100)

        payload = json.dumps({
            'numero': 19,
            'valor': 10
        })

        response = self.app.post('/render_juros', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual('Juros aplicados com sucesso!', response.data.decode('utf-8'))
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.TestLoader.sortTestMethodsUsing = lambda *args: -1
    unittest.main()