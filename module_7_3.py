class WordsFinder:
    def __init__(self, *args):
        self.file_names = [*args]
        self.file_name = args

    def get_all_words(self):
        all_words = {}
        symbols_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ', '  ', '—']
        for args in self.file_names:
            words = []
            with open(args, 'r', encoding='UTF-8') as file:
                for line in file:
                    line = line.lower()
                    for symbol in symbols_to_remove:
                        line = line.replace(symbol, '')
                    words += line.split()
                all_words[args] = words
        return all_words

    def find(self, word):
        places = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                places[name] = words.index(word.lower()) + 1

        return places

    def count(self, word):
        places = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                places[name] = words.count(word.lower())

        return places


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
