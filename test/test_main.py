import unittest
import requests


class TestMain(unittest.TestCase):
    def setUp(self):
        self.URL = "http://127.0.0.1:8080"
        self.data = {
            "Artist": "http://127.0.0.1:8080/artist?name=",
            "Character": "http://127.0.0.1:8080/character",
            "Episode": "http://127.0.0.1:8080/episode",
            "Favourites": "http://127.0.0.1:8080/favourites",
            "Home": "http://127.0.0.1:8080/"
        }

    def test_home(self):
        response = requests.get(self.URL)
        self.assertEqual(200, response.status_code)

    def test_inputType(self):
        response = requests.get(self.URL)
        self.assertIsInstance(response.json(), dict)

    def test_message(self):
        response = requests.get(self.URL)
        self.assertEqual(len(response.json()), 5)
        self.assertDictEqual(response.json(), self.data)


if __name__ == " __main__":
    unittest.main()
