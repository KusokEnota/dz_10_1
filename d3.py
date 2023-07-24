"""В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку."""


class WordCounter:
    def __init__(self, file_path, n=10):
        self.file_path = file_path
        self.n = n
        self.word_counts = {}

    def read_text_from_file(self):
        with open(self.file_path, encoding='utf-8') as f:
            text = f.read()
        text = "".join([i.lower() for i in text if i.isalpha() or i == " "])
        self.words = text.split()

    def count_words(self):
        for word in self.words:
            self.word_counts[word] = self.word_counts.get(word, 0) + 1

    def get_top_n_words(self):
        sorted_words = sorted(self.word_counts.items(), key=lambda x: (-x[1], x[0]))[:self.n]
        return sorted_words


if __name__ == "__main__":
    file_path = 'txt.txt'
    word_counter = WordCounter(file_path)
    word_counter.read_text_from_file()
    word_counter.count_words()

    top_n_words = word_counter.get_top_n_words()
    for word, count in top_n_words:
        print(f"Слово {word} встречается {count} раз")
