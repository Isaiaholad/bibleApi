import unittest
from bible_api.data import load_data
from bible_api.quiz import generate_quiz_question, generate_verse_count_quiz_question, generate_book_quiz_question, generate_word_quiz_question, generate_word_verse_quiz_question

class TestQuiz(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dataset = load_data()

    def test_generate_quiz_question(self):
        question, answers, correct = generate_quiz_question(self.dataset)
        self.assertIn('Which chapter and verse does this text belong to?', question)
        self.assertEqual(len(answers), 4)
        self.assertTrue(any(correct in answer for answer in answers))

    def test_generate_verse_count_quiz_question(self):
        question, answers, correct = generate_verse_count_quiz_question(self.dataset)
        self.assertIn('How many verses are in', question)
        self.assertEqual(len(answers), 4)
        self.assertTrue(any(str(correct) in answer for answer in answers))

    def test_generate_book_quiz_question(self):
        question, answers, correct = generate_book_quiz_question(self.dataset)
        self.assertIn('How many chapters does the book of', question)
        self.assertEqual(len(answers), 4)
        self.assertTrue(any(str(correct) in answer for answer in answers))

    def test_generate_word_quiz_question(self):
        question, answers, correct = generate_word_quiz_question('love', self.dataset)
        self.assertIn('How many times does the word', question)
        self.assertEqual(len(answers), 4)
        self.assertTrue(any(str(correct) in answer for answer in answers))

    def test_generate_word_verse_quiz_question(self):
        question, answers, correct = generate_word_verse_quiz_question('love', self.dataset)
        self.assertIn('In which verse does the word', question)
        self.assertEqual(len(answers), 4)
        self.assertTrue(any(correct in answer for answer in answers))

if __name__ == '__main__':
    unittest.main()
