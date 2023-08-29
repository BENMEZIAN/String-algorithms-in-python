# Python program for implementation of Aho-Corasick algorithm for string matching
import timeit

# For simplicity, Arrays and Queues have been implemented using lists.
# If you want to improve performance try using them instead

mycode='''
from collections import defaultdict
class AhoCorasick:
    def __init__(self, words):
        self.max_states = sum([len(word) for word in words])
        self.max_characters = 26
        self.out = [0]*(self.max_states+1)
        self.fail = [-1]*(self.max_states+1)
        self.goto = [[-1]*self.max_characters for _ in range(self.max_states+1)]
        
        for i in range(len(words)):
            words[i] = words[i].lower()

        self.words = words
        self.states_count = self.__build_matching_machine()

    # Builds the String matching machine.
    # Returns the number of states that the built machine has.
    # States are numbered 0 up to the return value - 1, inclusive.

    def __build_matching_machine(self):
        k = len(self.words)

        # Initially, we just have the 0 state
        states = 1

        # Convalues for goto function, i.e., fill goto
        # This is same as building a Trie for words[]
        for i in range(k):
            word = self.words[i]
            current_state = 0

            # Process all the characters of the current word
            for character in word:
                ch = ord(character) - 97  # Ascii value of 'a' = 97

                # Allocate a new node (create a new state)
                # if a node for ch doesn't exist.
                if self.goto[current_state][ch] == -1:
                    self.goto[current_state][ch] = states
                    states += 1

                current_state = self.goto[current_state][ch]

            # Add current word in output function
            self.out[current_state] |= (1 << i)

        # For all characters which don't have
        # an edge from root (or state 0) in Trie,
        # add a goto edge to state 0 itself
        for ch in range(self.max_characters):
            if self.goto[0][ch] == -1:
                self.goto[0][ch] = 0

        # Failure function is computed in
        # breadth first order using a queue
        queue = []

        # Iterate over every possible input
        for ch in range(self.max_characters):

            # All nodes of depth 1 have failure
            # function value as 0. For example,
            # in above diagram we move to 0
            # from states 1 and 3.
            if self.goto[0][ch] != 0:
                self.fail[self.goto[0][ch]] = 0
                queue.append(self.goto[0][ch])

        # Now queue has states 1 and 3
        while queue:

            # Remove the front state from queue
            state = queue.pop(0)

            # For the removed state, find failure
            # function for all those characters
            # for which goto function is not defined.
            for ch in range(self.max_characters):

                # If goto function is defined for
                # character 'ch' and 'state'
                if self.goto[state][ch] != -1:

                    # Find failure state of removed state
                    failure = self.fail[state]

                    # Find the deepest node labeled by proper
                    # suffix of String from root to current state.
                    while self.goto[failure][ch] == -1:
                        failure = self.fail[failure]

                    failure = self.goto[failure][ch]
                    self.fail[self.goto[state][ch]] = failure

                    # Merge output values
                    self.out[self.goto[state][ch]] |= self.out[failure]

                    # Insert the next level node (of Trie) in Queue
                    queue.append(self.goto[state][ch])

        return states

    # Returns the next state the machine will transition to using goto
    # and failure functions.
    # current_state - The current state of the machine. Must be between
    # 0 and the number of states - 1, inclusive.
    # next_input - The next character that enters into the machine.

    def __find_next_state(self, current_state, next_input):
        answer = current_state
        ch = ord(next_input) - 97  # Ascii value of 'a' is 97

        # If goto is not defined, use
        # failure function
        while self.goto[answer][ch] == -1:
            answer = self.fail[answer]

        return self.goto[answer][ch]

    # This function finds all occurrences of all words in text.

    def search_words(self, text):
        
        text = text.lower() # Convert the text to lowercase to make search case insensitive        
        current_state = 0 # Initialize current_state to 0

        # A dictionary to store the result.
        # Key here is the found word
        # Value is a list of all occurrences start index
        result = defaultdict(list)

        # Traverse the text through the built machine
        # to find all occurrences of words
        comparaison = 0
        for i in range(len(text)):
            comparaison += 1
            current_state = self.__find_next_state(current_state, text[i])

            # If match not found, move to next state
            if self.out[current_state] == 0:
                continue

            # Match found, store the word in result dictionary
            for j in range(len(self.words)):
                if (self.out[current_state] & (1 << j)) > 0:
                    word = self.words[j]

                    # Start index of word is (i-len(word)+1)
                    result[word].append(i-len(word)+1)
                    
        print("The number of comparaisons is :",comparaison)
                
        # Return the final result dictionary
        return result


# Driver code

words = ["Algo", "rithms"]
text = "Algorithms"

# Create an Object to initialize the Trie
aho_chorasick = AhoCorasick(words)

# Get the result
result = aho_chorasick.search_words(text)

# Print the result
for word in result:
    for i in result[word]:
        print('Word "{}" appears from {} to {}'.format(word, i, i+len(word)-1))
'''

exec_time = timeit.timeit(stmt=mycode,number=1) * 10**3
print(f"The time of execution of above program is : {exec_time:.03f}ms")





