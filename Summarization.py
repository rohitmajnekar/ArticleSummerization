import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


class Summarization:
    def __init__(self):
        self.stopwords = STOP_WORDS
        self.nlp = spacy.load('en_core_web_sm')
        self.punctuation = punctuation + '\n'

    def tokenization(self, string):
        self.doc = self.nlp(string)
        self.tokens = [token.text for token in self.doc]

    def frequency(self):
        self.word_frequencies = {}
        for word in self.doc:
            if word.text.lower() not in self.stopwords:
                if word.text.lower() not in self.punctuation:
                    if word.text not in self.word_frequencies.keys():
                        self.word_frequencies[word.text] = 1
                    else:
                        self.word_frequencies[word.text] += 1
        max_frequency = max(self.word_frequencies.values())
        for word in self.word_frequencies.keys():
            self.word_frequencies[word] = self.word_frequencies[word] / max_frequency
        self.sentence_tokens = [sent for sent in self.doc.sents]

    def result(self):
        sentence_scores = {}
        for sent in self.sentence_tokens:
            for word in sent:
                if word.text.lower() in self.word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = self.word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += self.word_frequencies[word.text.lower()]

        select_length = int(len(self.sentence_tokens) * 0.3)
        select_length
        summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
        final_summary = [word.text for word in summary]
        summary = ' '.join(final_summary)
        print(summary)
        # with open('test.txt', 'a+', encoding='utf-8') as file:
        #     file.writelines(["%s\n", summary])
        return summary

    def summerize(self, string):
        self.tokenization(string)
        self.frequency()
        return self.result()



