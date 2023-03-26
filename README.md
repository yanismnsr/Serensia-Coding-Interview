# Serensia-Coding-Interview

This project implements a python class, `WordSuggestor`, that is responsible of returning, from a list of words, the ones that are most similar to a given word. To reach this, it uses a similarity algorithm which is implemented in the `GetDifferenceScore` function that you can find in `src/common/utils.py`

## Usage :
```python
import src.WordSuggestor as ws

suggestor = ws.WordSuggestor()

term = "gros"
words = ["gros", "grise", "gras", "graisse", "aggressif", "go"]
print(suggestor.GetSuggestions(term, words, 2)) # ["gros", "gras"]
```

You can also run the `main.py` with the following command:
```bash
python3 main.py
```

## Unit tests
You can find the unit tests of the project in the `test/test.py` file. You can add your tests and run them with the following command :

```python
python3 -m unittest test.test
```

Make sure to be in the root folder of the project when running the command