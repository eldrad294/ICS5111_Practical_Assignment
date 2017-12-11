from src.visual.visual_handler import visual
#visual().bar_handler()
# visual().boxplot_handler()
# visual().pieplot_handler()
from src.textprocessing.SentimentAnalyzer import SentimentAnalyzer
sa = SentimentAnalyzer()
pred = sa.predict("""We had an amazing time.  Wanted something fun for the kids and this was perfect.  The staff was extremely nice.  Even volunteered to watch our 2 year old so the family (10 of us) could race together.  Cars were fast, reliable and just a really good time.  Thanks for the fun memories.""")
print(pred)
print(sa.accuracy())