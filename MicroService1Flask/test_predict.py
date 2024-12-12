import unittest
import json
from svm_service import app 

class TestPredictEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_missing_wav_music(self):
        response = self.app.post('/predict', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Le paramètre 'wav_music' est manquant.", response.get_json().get('error'))

    def test_invalid_base64(self):
        invalid_data = {"wav_music": "invalid_base64_string"}
        response = self.app.post('/predict', json=invalid_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Error decoding base64", response.get_json().get('error'))

if __name__ == "__main__":
    unittest.main()
