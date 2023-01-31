
class google_suggest():
    def __init__(self, words_file=None):
        if not words_file:
            self.words_file = 'words_alpha.txt'
        else:
            self.words_file = words_file
        self.words_dict = self.create_prefix_word_dict()

    def create_prefix_word_dict(self):
        with open(self.words_file) as f:
            words = f.read()
        
        word_list = words.split('\n')
        possible_completions_dict = {}

        for word in word_list:
            for index in range(1, len(word)):
                if not possible_completions_dict.get(word[0:index]):
                    possible_completions_dict[word[0:index]] = [word]
                else:
                    possible_completions_dict[word[0:index]].append(word)
        
        return possible_completions_dict


    def possible_completions(self, letter_string):

        if len(letter_string) == 0:
            raise ValueError("string must be at least 1 character long")
        
        return self.possibble_completion_dict[letter_string]


    def print_possible_completions(self, prefix):
        print(self.words_dict[prefix])


def main():
    suggest_obj = google_suggest()
    suggest_obj.print_possible_completions("tank")



if __name__ == "__main__":
    main()
