import unittest
from bible_api.data import load_data

class TestData(unittest.TestCase):

    def test_load_data(self):
        dataset = load_data()
        self.assertFalse(dataset.empty)
        self.assertIn('book', dataset.columns)
        self.assertIn('chapter', dataset.columns)
        self.assertIn('verse', dataset.columns)
        self.assertIn('text', dataset.columns)

if __name__ == '__main__':
    unittest.main()
