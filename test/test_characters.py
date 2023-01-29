import unittest
import requests


class TestCharacters(unittest.TestCase):
    def setUp(self):
        self.URL = "http://127.0.0.1:8080/character"
        self.Morty='Morty Smith'
        self.location='Interdimensional Cable'

    def test_home(self):
        response = requests.get(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_all(self):
        response = requests.get(self.URL)
        self.assertEqual(len(response.json()), 20)

    def test_Morty(self):
        response = requests.get(self.URL)
        self.assertEqual(response.json()[1]['Name'], self.Morty)

    def test_location(self):
        response = requests.get(self.URL)
        self.assertEqual(response.json()[19]['Location'], self.location)


if __name__ == " __main__":
    unittest.main()
