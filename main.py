import src.WordSuggestor as ws

def main():
    suggestor = ws.WordSuggestor()
    print(suggestor.GetSuggestions("gros", ["gros", "grise", "gras", "graisse", "aggressif", "go"], 2))

if __name__ == "__main__":
    main()