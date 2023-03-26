import unittest
import src.WordSuggestor as ws

class TestWordSuggestor(unittest.TestCase):
    def test_given_example(self):
        term = "gros"
        choices = ["gros", "gras", "graisse", "aggressif", "go", "ros", "gro"]
        numberOfSuggestions = 2
        suggestor = ws.WordSuggestor()
        self.assertEqual(suggestor.GetSuggestions(term, choices, numberOfSuggestions), ["gros", "gras"])

    def test_empty_choices(self):
        term = "gros"
        choices = []
        numberOfSuggestions = 2
        suggestor = ws.WordSuggestor()
        self.assertEqual(suggestor.GetSuggestions(term, choices, numberOfSuggestions), [])

    def test_empty_term(self):
        term = ""
        choices = ["gros", "gras", "graisse", "aggressif", "go", "ros", "gro"]
        numberOfSuggestions = 2
        suggestor = ws.WordSuggestor()
        self.assertEqual(suggestor.GetSuggestions(term, choices, numberOfSuggestions), [])
    
    def test_numberOfSuggestions_longer_than_length(self):
        term = "sirene"
        choices = ["sauron", "serensia"]
        numberOfSuggestions = 4
        suggestor = ws.WordSuggestor()
        self.assertEqual(suggestor.GetSuggestions(term, choices, numberOfSuggestions), ["serensia", "sauron"])


if __name__ == '__main__':
    unittest.main()