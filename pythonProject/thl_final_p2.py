class FiniteAutomaton:
    def __init__(self, transitions, initial_state, final_states):
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def recognize(self, word):
        current_state = self.initial_state
        for char in word:
            if (current_state, char) in self.transitions:
                current_state = self.transitions[(current_state, char)]
            else:
                return False
        return current_state in self.final_states

def main():
    transitions = {
        (0, 'a'): 1,
        (0, 'b'): 2,
        (1, 'a'): 3,
        (1, 'b'): 4,
        (4, 'a'): 1,
        (4, 'b'): 2,
    }
    initial_state = 0
    final_states = {2, 3}

    automaton = FiniteAutomaton(transitions, initial_state, final_states)

    word = input("Entrez un mot à reconnaître: ")
    if automaton.recognize(word):
        print("Le mot est reconnu par l'automate.")
    else:
        print("Le mot n'est pas reconnu par l'automate.")

if __name__ == "__main__":
    main()
