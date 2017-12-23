from src.visual.visual_handler import visual
# if __name__ == '__main__':
#     visual().bar_handler()
# visual().boxplot_handler()
# visual().pieplot_handler()
#
# ----------------------------------------
#
#from src.textprocessing.SentimentAnalyzer_NB_NLTK import SentimentAnalyzer
from src.textprocessing.SentimentAnalyzer_LogisticRegression import SentimentAnalyzer
sa = SentimentAnalyzer()
#sentence = 'Eh. Unimpressed. Poor waitresses look overworked- we had to ask the manager for refills, got my order wrong twice. Breakfast was a little bland (we got the healthy options & apparently that means no flavor) You have many other better and more delicious options nearby. Sorry morning squeeze, work more on your food and service instead of putting all your effort in a trendy vibe.'
#sentence = 'Pizza here made my night... Good people and great pizza. They can do anything you ask with a great attitude!'
#sentence = "Super good food! My friends and I ordered 2 lbs of shrimp, 2 lbs of crab legs, 2 Cajun fries, sweet potato fries, calamari, and fried catfish! We ate it allllll up. My only concern was that the crabs were a bit difficult to crack but then again I'm used to cracking the Alaskan crab legs. But other than the difficult cracking, the mix of all the seasonings was just a great fusion of flavors to really individualize their seafood from anything I've ever tried. And it was not primetime when we went so service was pretty fast! Hope they're on top of their game when it is busy!"
#sentence = "I waited for my order for over 10 minutes. I ordered two chicken finger kids meals and two adult meals. Had to pull forward and wait another ten minutes for food. When I got home they didn't give me my kids meals."
#sentence = "This place is definitely for hipsters, which me and my boyfriend are not. It is well decorated and feels really 'cool' but the food wasn't anything to rave about. One of those places that people go to just to say they've been there, I guess. I went for dinner, and the dinner menu is actually smaller than their lunch menu? I thought that was weird. All the things that I saw on yelp reviews and I actually wanted to try were not for sale at the time I went. I settled and had curry, it was alright. So they get an okay review, because everything there was okay. Nothing bad, just nothing special. Oh I lied, there was one thing that was pretty great. We paid four bucks for their self-filtered water and it was actually really amazing. LOL. I know that sounds like I totally got ripped off but the water was literally tasteless it felt so weird to drink. Quite the experience. I wouldn't go back for water, but I am glad I tried it once!"
#sentence = "Very unimpressed by their pad Thai.. one of the worst I have had.. lacks flavor and beef tastes like rubber.. I ordered though UberEATS so I don't know if in store it's different but won't be returning for sure!"
#sentence = "I had the pork shank and ate the whole thing. Too bad for my waist line but excellent choice for my belly! it could have fed two and fell off the bone. Delicious."
sentence = 'Bad bad customer service!!  I was willing to give this place a try. Came in to make some purchases and was completely ignored. Employees were busy conversing among themselves. Waited for about 15minutes for them and was told "some one will be with you shortly" so i just walked out. Best if you take business to Healy or AZ guns!'
pred = sa.predict(sentence)
print(pred)
#print(sa.test_set())
#
# ---------------------------------------
#
# from src.db.core import Core
# c = Core()
#
#c.populate_table_business_user_sentiment()
#
# time = ['Sunday','10:00']
# coordinates = [43.8409,-79.3996]
# c.get_suggested_businesses('Food',coordinates,time,100)
#
# c.get_business_cluster('state')