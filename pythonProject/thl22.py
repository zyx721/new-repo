import random

class RegularGrammar:
    def __init__(self, rules):
        self.rules = rules

    def generate_word(self, start_symbol, length=None):
        if length is None:
            return self._generate_from_symbol(start_symbol)
        else:
            return self._generate_from_symbol_with_length(start_symbol, length)

    def _generate_from_symbol(self, symbol):
        if symbol not in self.rules:
            return symbol  # It's a terminal symbol
        production = random.choice(self.rules[symbol])
        return ''.join(self._generate_from_symbol(sym) for sym in production)

    def _generate_from_symbol_with_length(self, symbol, length):
        if length == 0:
            if symbol in self.rules:
                if '' in self.rules[symbol]:
                    return ''
                else:
                    raise ValueError("Cannot generate word of length 0 from non-terminal symbol without empty production")
            else:
                raise ValueError("Cannot generate word of length 0 from terminal symbol")
        if symbol not in self.rules:
            raise ValueError("Cannot generate word of given length from terminal symbol")
        production = random.choice(self.rules[symbol])
        word = ''
        for sym in production:
            if len(word) < length:
                word += self._generate_from_symbol_with_length(sym, length - len(word))
        if len(word) > length:
            word = word[:length]
        return word

    def is_word_in_language(self, word):
        stack = [('S', word)]
        while stack:
            symbol, remaining_word = stack.pop()
            if symbol == '':
                if not remaining_word:
                    return True
                continue
            if not remaining_word:
                continue
            if symbol in self.rules:
                for production in self.rules[symbol]:
                    if remaining_word.startswith(production):
                        stack.append((production, remaining_word[len(production):]))
        return False


def main():
    rules = {
        'S': ['aS', 'aA', ''],
        'A': ['bA', 'b']
    }
    grammar = RegularGrammar(rules)

    print("Generating words:")
    n = int(input("Enter the number of words to generate: "))
    for _ in range(n):
        print(grammar.generate_word('S'))

    # Recognizer
    word_to_check = input("Enter a word to check if it belongs to the language: ")
    if grammar.is_word_in_language(word_to_check):
        print("The word belongs to the language.")
    else:
        print("The word does not belong to the language.")

if __name__ == "__main__":
    main()
