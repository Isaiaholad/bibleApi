import unittest
from bible_api.data import load_data
from bible_api.analysis import find_longest_and_shortest_chapters, rearrange_chapters_by_verse_count, identify_common_words_and_phrases, list_top_20_most_common_phrases, list_top_20_shortest_verse_text

class TestAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dataset = load_data()

    def test_find_longest_and_shortest_chapters(self):
        longest, shortest = find_longest_and_shortest_chapters(self.dataset)
        self.assertIsNotNone(longest)
        self.assertIsNotNone(shortest)

    def test_rearrange_chapters_by_verse_count(self):
        sorted_chapters = rearrange_chapters_by_verse_count(self.dataset)
        self.assertFalse(sorted_chapters.empty)
        self.assertIn('book', sorted_chapters.columns)
        self.assertIn('chapter', sorted_chapters.columns)
        self.assertIn('verse_count', sorted_chapters.columns)

    def test_identify_common_words_and_phrases(self):
        common_words = identify_common_words_and_phrases(self.dataset)
        self.assertGreater(len(common_words), 0)

    def test_list_top_20_most_common_phrases(self):
        common_phrases = list_top_20_most_common_phrases(self.dataset)
        self.assertEqual(len(common_phrases), 20)

    def test_list_top_20_shortest_verse_text(self):
        shortest_verses = list_top_20_shortest_verse_text(self.dataset)
        self.assertEqual(len(shortest_verses), 20)

if __name__ == '__main__':
    unittest.main()
