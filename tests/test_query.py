import unittest
from bible_api.data import load_data
from bible_api.query import get_total_chapters, get_total_verses, query_text, search_verses, count_keyword_occurrences

class TestQuery(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dataset = load_data()

    def test_get_total_chapters(self):
        total_chapters = get_total_chapters('Genesis', self.dataset)
        self.assertEqual(total_chapters, 50)

    def test_get_total_verses(self):
        total_verses = get_total_verses('Genesis', 1, self.dataset)
        self.assertEqual(total_verses, 31)

    def test_query_text(self):
        text = query_text('Genesis', 1, self.dataset, [1])
        self.assertEqual(len(text), 1)
        self.assertIn('In the beginning', text[0])

    def test_search_verses(self):
        results = search_verses('love', self.dataset)
        self.assertGreater(len(results), 0)

    def test_count_keyword_occurrences(self):
        count = count_keyword_occurrences('love', self.dataset)
        self.assertGreater(count, 0)

if __name__ == '__main__':
    unittest.main()
