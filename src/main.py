from src.visual.visual_handler import visual
#visual().bar_handler()
# visual().boxplot_handler()
# visual().pieplot_handler()
from src.textprocessing.SentimentAnalyzer_NB_NLTK import SentimentAnalyzer
sa = SentimentAnalyzer()
pred = sa.predict("""Eh. Unimpressed. Poor waitresses look overworked- we had to ask the manager for refills, got my order wrong twice. Breakfast was a little bland (we got the healthy options & apparently that means no flavor) You have many other better and more delicious options nearby. Sorry morning squeeze, work more on your food and service instead of putting all your effort in a trendy vibe.""")
print(pred)
print(sa.test_set())