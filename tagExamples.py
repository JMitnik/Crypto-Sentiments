from VUtagger import *
config = Namespace(lexicon='resources/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt',
                   tags=['anger', 'anticipation', 'disgust', 'fear', 'joy', 'negative', 'positive', 'sadness',
                         'surprise', 'trust'],
                   text="It was one of the worst movies I've seen, despite good reviews.")
tag(config)


from NRC import *
model = 'resources/model.p'
lexicon = 'resources/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt'
emo = EmotionModel(model, lexicon)
print(emo.predict("It was one of the worst movies I've seen, despite good reviews."))

