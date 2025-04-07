import unittest
from todo_project import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_404_page(self):
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()