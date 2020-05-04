class ReverseWord(object):
    def __init__(self, word):
        self.word = word
    
    def perform_rev_word(self):
        ''' Reverse a word '''
        rev_word=''
        # for i in range(-1, -1*len(word)-1, -1):
        for i in range(len(self.word)-1,-1, -1):
            rev_word += self.word[i]
        return rev_word

class ReverseSentence(object):
    def __init__(self, sentence):
        self.sentence = sentence

    def perform_rev_sentn(self):
        ''' Reverse a sentense '''
        rev_sentn=''
        main_sent = self.sentence.split()
        for i in range(len(main_sent)-1, -1, -1):
            rev_sentn += main_sent[i] + " "
        return rev_sentn

if __name__ == "__main__":
    reverse_word = ReverseWord("Hello")
    print(reverse_word.perform_rev_word())
    reverse_sent = ReverseSentence("Hello World")
    print(reverse_sent.perform_rev_sentn())