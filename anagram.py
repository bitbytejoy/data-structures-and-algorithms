def is_anagram(word_1, word_2):
    if len(word_1) != len(word_2):
        return False
    letters_1 = {}
    letters_2 = {}
    for letter in word_1:
        if letters_1.get(letter) == None:
            letters_1[letter] = 0
        letters_1[letter] += 1
    for letter in word_2:
        if letters_2.get(letter) == None:
            letters_2[letter] = 0
        letters_2[letter] += 1
    for letter in letters_1:
        if letters_2.get(letter) != letters_1[letter]:
            return False
    return True

import unittest
class AnagramTests(unittest.TestCase):
    def test_not_anagram(self):
        self.assertFalse(is_anagram("Test", "Not"))
    def test_not_anagram_case_sensitive(self):
        self.assertFalse(is_anagram("Test", "stte"))
    def test_is_anagram(self):
        self.assertTrue(is_anagram("Test", "sTte"))

if __name__ == "__main__":
    unittest.main()
