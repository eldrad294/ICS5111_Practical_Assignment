from src.textprocessing.SentimentAnalyzer import SentimentAnalyzer
#
sa = SentimentAnalyzer()
pred = sa.predict("I will never go there again")
print(pred)