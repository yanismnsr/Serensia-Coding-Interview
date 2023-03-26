import src.common.utils as utils

class IAmTheTest:
    def GetSuggestions(self, term, choices, numberOfSuggestions):
        pass
    
class WordSuggestor (IAmTheTest):
    def GetSuggestions(self, term, choices, numberOfSuggestions):
        scores = [(choice, len(choice), utils.GetDifferenceScore(term, choice)) for choice in choices]
        scores = [score for score in scores if score[2] != -1]
        scores.sort(key=lambda x: (x[2], x[1]))
        return [score[0] for score in scores[:min(numberOfSuggestions, len(scores))]]