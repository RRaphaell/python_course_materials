import unittest

from palindrome import is_palindrome
from spelling import get_correct_text
from find_char import char_in_word


class Test(unittest.TestCase):

    def test_palindrome_1(self):
        self.assertEqual(True, is_palindrome("level"))

    def test_palindrome_2(self):
        self.assertEqual(False, is_palindrome("qwe"))

    def test_palindrome_3(self):
        self.assertEqual(True, is_palindrome("r"))

    def test_spelling_1(self):
        text = "A man paralyzed from the neck down due to a spinal cord injury thanks to a brain implant system that translates his imagined handwriting into actual text."
        converted_text = " ".join([word.capitalize() for word in text.split()])
        self.assertEqual(converted_text, get_correct_text(text))

    def test_find_char_1(self):
        text = "python"
        char = "p"
        self.assertEqual(char in text, char_in_word(text, char))

    def test_find_char_2(self):
        text = "python"
        char = "P"
        self.assertEqual(char in text, char_in_word(text, char))

    def test_find_char_3(self):
        text = "python"
        char = "j"
        self.assertEqual(char in text, char_in_word(text, char))


if __name__ == '__main__':
    unittest.main()
