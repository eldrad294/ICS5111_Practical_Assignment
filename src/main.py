from src.visual.visual_handler import visual
#visual().bar_handler()
# visual().boxplot_handler()
# visual().pieplot_handler()
from src.textprocessing.SentimentAnalyzer import SentimentAnalyzer
sa = SentimentAnalyzer()
pred = sa.predict("Allegiant is a disaster.  Their fares are cheap, but not cheap enough.  Our flight out of Las Vegas was scheduled to leave at 11:00 am.  We boarded and were told to de-plane because of an electrical problem.  After four hours, we get back on, only to be told that the problem hasn't been resolved.  Off again.  Eventually, we're told they are getting us a different plane and that we will take off at 6:00.  We'll see. The issue is not that there was a problem with an Allegiant flight.  The issue is the consistency with which this airline has problems.  I do not believe it is an exaggeration to say that half of its flights are delayed or cancelled. Update:  6:30 pm and the boarding estimate is now 7:50 pm.")
print(pred)