from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QWidget
from trie import Trie
from spell_correction import suggest_corrections
from web_scraper import fetch_definition

class DictionaryApp(QMainWindow):
    def __init__(self, trie, dictionary):
        super().__init__()
        self.trie = trie
        self.dictionary = dictionary
        self.setWindowTitle("English Word Lookup")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.input_box = QLineEdit(self)
        layout.addWidget(self.input_box)

        self.search_button = QPushButton("Search", self)
        self.search_button.clicked.connect(self.search_word)
        layout.addWidget(self.search_button)

        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)
        layout.addWidget(self.output_area)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def search_word(self):
        word = self.input_box.text().strip().lower()
        if word:
            if self.trie.search(word):
                self.output_area.setText(f"'{word}' is a valid word.")
            else:
                suggestions = suggest_corrections(word, self.dictionary)
                definition = fetch_definition(word)
                self.output_area.setText(f"'{word}' not found.\n\nSuggestions: {', '.join(suggestions)}\n\nDefinition: {definition}")

if __name__ == '__main__':
    # Load dictionary
    trie = Trie()
    dictionary = []
    with open('data/dictionary_words.txt', 'r') as file:
        for line in file:
            word = line.strip()
            trie.insert(word)
            dictionary.append(word)

    app = QApplication([])
    window = DictionaryApp(trie, dictionary)
    window.show()
    app.exec()
