import os
import pickle
from collections import defaultdict, Counter
from nltk import word_tokenize

class EmotionModel:
    """Detects emotion and sentiment in a text using
    NRC Word-Emotion Association Lexicon
    (NRC Emotion Lexicon)
    Version 0.92
    Copyright (C) 2011 National Research Council Canada (NRC)
    Contact: Saif Mohammad (saif.mohammad@nrc-cnrc.gc.ca)
    """
    def __init__(self, model, lexicon):
        """Load the lexicon pickle, create the pickle if it not exists"""
        if os.path.exists(model):
            self.model = pickle.load(open(model, "rb"))
        else:
            self.model = self.create_model(model, lexicon)
    def create_model(self, model, filename):
        """Create the pickle, TODO, what is the location of the lexicon"""
        lexicon = defaultdict(dict)
        with open(filename, 'r') as f:
            for line in f:
                try:
                    cols = line.strip().split()
                    lexicon[cols[0]][cols[1]] = int(float(cols[2]))
                except Exception as e:
                    print("Whoops")
        pickle.dump(lexicon, open(model, "wb"))
        return lexicon
    def predict(self, text):
        """Predict the sentiment and emotion of a text"""
        emotion_fields = [
            'anger',
            'anticipation',
            'disgust',
            'fear',
            'joy',
            'sadness',
            'surprise',
            'trust',
        ]
        sentiment_fields = [
            'negative',
            'positive'
        ]
        count = Counter()
        for token in word_tokenize(text.lower()):
            if token in self.model:
                count += Counter(self.model[token])
        # get % per emotion
        emotion_score = {}
        for key in emotion_fields:
            emotion_score[key] = count[key]
        emotion_perc = {}
        for key in emotion_fields:
            emotion_perc[key] = self.calculate_perc(count[key], sum(emotion_score.values()))
        # get % per sentiment
        sent_score = {}
        for key in sentiment_fields:
            sent_score[key] = count[key]
        sent_perc = {}
        for key in sentiment_fields:
            sent_perc[key] = self.calculate_perc(count[key], sum(sent_score.values()))
        return {
            'emotion_cnt': emotion_score,
            'emotion': emotion_perc,
            'sentiment_cnt': sent_score,
            'sentiment': sent_perc
        }
    @staticmethod
    def calculate_perc(val, total):
        try:
            value = val / total
        except ZeroDivisionError:
            value = 0
        return value

if __name__ == '__main__':
    model='resources/model.p'
    lexicon='resources/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt'
    emo = EmotionModel(model,lexicon)
    print(emo.predict("It was one of the worst movies I've seen, despite good reviews."))
