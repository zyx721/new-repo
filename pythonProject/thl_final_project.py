import random

class RegularGrammar:
    def __init__(self, rules):
        self.rules = rules

    def _generate_from_symbol(self, symbol):
        if symbol not in self.rules:
            return symbol  # It's a terminal symbol
        production = random.choice(self.rules[symbol])
        return ''.join(self._generate_from_symbol(sym) for sym in production)

def main():
    rules = {
        'S': ['aS', 'aA'],
        'A': ['bA', 'b']
    }
    grammar = RegularGrammar(rules)

    print("Generating words:")
    n = int(input("Enter the number of words to generate: "))
    for _ in range(n):
        print(grammar._generate_from_symbol('S'))

if __name__ == "__main__":
    main()
